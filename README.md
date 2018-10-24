# DataMining_HW1

This project use 3 dataset to implement Apriori Algorithm with FP-Growth
1. Dataset from Power Point im class
2. IBM Quest Data Generator
3. Kaggle dataset(https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings)

## IF you are Teacher or TA
Please read report [Report.pdf](https://github.com/ooxx5626/DataMining_FP-Growth/blob/master/Report.pdf)


## Getting Started
Select your data in start.py
```
do_IBMData() //or
do_KaggleData()
```

Start by start.py .

```
python3 start.py
```
## Show Time
There is 3 step in data print
### First Step
The Frequent Itemset with min_sup 

![](https://i.imgur.com/5JjftCZ.png)
### Second Step
FP-tree

![](https://i.imgur.com/h0P9hOP.png)
### Third Step
Associate Rules

![](https://i.imgur.com/MPrPRv9.png)
## Compare
We can use [ WEKA ](https://www.cs.waikato.ac.nz/ml/weka/) ayanalysis our data
### Data format
***WEKA mandate data format, not all CSV data can be input!!***

Maybe you can use ARFF data 

***example***

![](https://i.imgur.com/8a2HGZc.png)

more detail is in WEKA doc 10.1

 relation names or attribute names 
 
 ``` 
 ’{’, ’}’, ’,’, or ’%’
 ```
 
### Ayanalysis

1. WEKA >> associate >> choose FP-Growth
2. Setting your parameter
3. Start!!


![](https://i.imgur.com/egXGkGf.png)

## Enjoy
