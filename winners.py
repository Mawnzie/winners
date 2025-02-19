


import pandas as pd


class EmptyDataframeException(Exception):
    pass



def read_csv(file):
    df = pd.read_csv(file, sep = ";",parse_dates=True)

    if  df.empty !=True and df.Kurs.dtype != 'float64':
        raise ValueError("Kurs får bara innehålla reella tal.")
    elif df.empty ==True:
        raise EmptyDataframeException("The dataframe is empty")
    df=df.rename(columns={'Kod':'name'})
    df['Time'] = pd.to_datetime(df['Date']).dt.time
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    return df

def parse_csv(file):
    try:
        df = read_csv(file)


    except pd.errors.EmptyDataError as e:
        print(e)
    except EmptyDataframeException as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        #only keep the entries for today
        idx = df[df['Date'] == df['Date'].max()].index
        df = df.iloc[idx]
        #Drop 'Date' column:
        df = df.drop(['Date'],axis=1)
        
    
        
        #Dataframes with the first and last entries for each stock:
        dffirst = df.groupby(by='name',as_index=False).first()
        dflast = df.groupby(by='name',as_index=False).last()
        
        
        dffirst = dffirst.rename(columns={"Kurs":"first"})
        dflast = dflast.rename(columns={"Kurs":"latest"})
        
        dffirst=dffirst.drop(columns=['Time'])
        dflast = dflast.drop(columns=['Time'])
        
        
        dfmerged = pd.merge(dffirst,dflast,on='name')
        
        #Lägg till kolumn med aktiekursens utveckling:
        dfmerged['percent'] = dfmerged['latest']/dfmerged['first']
        
        
        
        dfmerged['rank'] = dfmerged['percent'].rank(ascending=False)
        
        #Sortera dfmerged efter 'Utveckling'
        dfsorted =dfmerged.sort_values(by=['percent'],ascending=False)
        
        
        """
        Behåll aktierna med bäst utveckling:
        (Vi använder '<4' eftersom vi tillåter delad rank om två aktier har samma utveckling. 
        Detta är möjligt om det t.ex. bara finns en datapunkt för dagens datum.)
        """
        dfsorted =dfsorted[dfsorted['rank']<4]
        
        #Ta bort kolumnen med dagens första värde:
        dfsorted = dfsorted.drop(['first'],axis=1)
        
        #Visa kursutveckling i % med 6 decimaler:
        dfsorted['percent'] = dfsorted['percent'].apply(lambda x: f"{x-1:.2%}")
        
        
        #Aktier med delad rank får heltalsrank (e.g. 3.5 blir 3).
        dfsorted['rank'] = dfsorted['rank'].apply(lambda x:int(x))
        return dfsorted

   
if __name__=="__main__":
    import sys
    dfsorted = parse_csv(sys.argv[1])
    out = dfsorted.to_json(orient='records',indent=4)
    out = '{"winners": \n ' +out +'\n}'
    with open('winners.json', 'w') as f:
        f.write(out)


