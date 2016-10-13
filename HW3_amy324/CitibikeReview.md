# Citibike mini project review by fb55    

## IDEA: the idea is fine                                                             

Customers are less likely than Subscribers to choose biking on weekdays

## Null: the null is the complement of what you are putting forward in your idea! if you suspect that cistomers are LESS likely then the null must say costumers are MORE OR EQUALLY likely (the complement of what you expect to see) and you try to falsify that. (or since you phrased is as Subscribers, the ratio of Subscribers riding over weekend to riding over weeks is equal or less )

 "The ratio of Subscribers biking on weekends over Subscribers biking on weekdays is the same or **lower** than the ratio of Customers biking over weekends to Customers biking on weekdays

Cust_wend/Cust_wdays >= Subs_wend/Subs_wdays 

etc

## Data wrangling:

```
#Lets make Customer = 0, Subscriber  = 1
df.usertype = df.usertype.replace('Customer', 0)
df.usertype = df.usertype.replace('Subscriber', 1)
df.head()
```

this is not necessary since pandas deals with categorical data well. If you were using numpy you would need to do something like that at some point 9most likely) but with pandas it is probably not needed

## each figure needs its caption!

very good: you see, to see an effect. you should consolidate all week days and all weekend days, and normalize appropriately, then you are all set for a test of proportions (chi sq)


