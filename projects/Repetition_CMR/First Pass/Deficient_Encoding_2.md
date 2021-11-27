# <center>An Independent Effect of Deficient Processing for List Memory?

### Background
The big idea of the deficient encoding hypothesis as an account of the spacing effect is that:
1. Item familiarity ("close acquaintance") impairs attention and memory of subsequent encoding.
2. Repeated experience of an item increases familiarity with that item
3. On the other hand, familiarity decreases with intervening experience, allowing better memory of repetitions
    
The MINERVA-DE model (Collins et al, 2020) implements a model with these mechanisms to account for various effects in recognition memory. In the model, a short-term memory store called primary memory is maintained with a long-term secondary memory. When a word is attended, its familiarity is computed relative to the items in primary memory. The more familiar a studied item is to existing items in primary memory, the less well it is encoded in secondary memory. This process is called discrepancy encoding, because encoding is strongest for items that are discrepant with information already stored in primary memory.

I was interested in motivating a similar mechanism within the framework of retrieved context theory.

- Review spacing effect
- Review retrieved context theory and work relating it to spacing effect
- Review deficient encoding account of effect
- State that an account of repetition effects integrating these frameworks has so far gone unexplored.
- Draw a diagram outlining what such an account might look like

### Hypothesis
If during a free recall task
1. Short-term familiarity mediates memory for item repetitions as outlined above,
2. Short-term familarity itself is mediated by a representation of temporal context reflecting "a recency-weighted average of information related to recently presented stimuli", and
3. Studying an item prompts retrieval and reinstatement of previous contextual associations

Then for an item $A$ originally presented at position $i$ during study, repetition of an item $B$ originally presented at position $i+1$ should enhance short-term familiarity with $A$ by prompting retrieval of shared contextual associations. This in turn, should drive an independent spacing effect between positions of the second presentation of $B$ and a later second presentation of $A$.

### ...But a Problem
This conceptualization effectively ties short-term familarity to contextual variability, making it impossible to tease apart the two accounts. Unfortunately, I tried testing this hypothesis as posed anyway!




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>subject</th>
      <th>list</th>
      <th>item</th>
      <th>input</th>
      <th>output</th>
      <th>study</th>
      <th>recall</th>
      <th>repeat</th>
      <th>intrusion</th>
      <th>condition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>False</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2.0</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>False</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>3.0</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>False</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>4.0</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>False</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>5.0</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>False</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### Approach

I searched for evidence of this pattern using data from Lohnas (2014), particularly in trials consisting of pure spaced lists with length 40, consisting of items presented twice at lags 1-8, where lag is defined as the number of intervening items between a repeated item's presentations. In the pure spaced lists, spacings of repeated items were chosen so that each of the lags 1-8 occurred with equal probability.

I identified all trials in the dataset with $A, B, ..., B, A$ subsequences, with no multiple presentations of a single item between $AB$ and $BA$. I also required at least one intervening item between presentations of $B$.

For comparison and to control for possible serial position or spacing effects, I matched identified trials to ones in the dataset where serial position, subject id, and lag between presentations of $A$ were identical, but a lag was present between second presentations of $B$ and of $A$: $A, B, ..., B, ..., A$. Where multiple matching trials could be found for a given $A, B, ..., B, A$, we enforced downstream comparison outcomes to reflect an weighted average of all of them.

### Results

### Matching Features
We define a new function that finds matching subsequences this way.

### Building a DataFrame
For every subsequence in group 0 that we can find matching subsequences for in other groups (should we care if it's in all other groups? Figure that out later), we'll sample from the retrieved subsequences 100 times to build a dataframe with our controls.

I wonder if I can type this stuff and get a result?




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>trial</th>
      <th>list_type</th>
      <th>subject</th>
      <th>group</th>
      <th>item</th>
      <th>recalled</th>
      <th>startPos</th>
      <th>lagA</th>
      <th>lagB</th>
      <th>lagB1</th>
      <th>lagB2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>No Lag Between Second B and A</td>
      <td>5</td>
      <td>True</td>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>No Lag Between Second B and A</td>
      <td>5</td>
      <td>True</td>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>No Lag Between Second B and A</td>
      <td>5</td>
      <td>True</td>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>No Lag Between Second B and A</td>
      <td>5</td>
      <td>True</td>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>No Lag Between Second B and A</td>
      <td>5</td>
      <td>True</td>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>trial</th>
      <th>list_type</th>
      <th>subject</th>
      <th>group</th>
      <th>item</th>
      <th>recalled</th>
      <th>startPos</th>
      <th>lagA</th>
      <th>lagB</th>
      <th>lagB1</th>
      <th>lagB2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>Lag Between Second B and A</td>
      <td>6</td>
      <td>False</td>
      <td>7</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>101</th>
      <td>31</td>
      <td>3</td>
      <td>1</td>
      <td>Lag Between Second B and A</td>
      <td>4</td>
      <td>False</td>
      <td>7</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>102</th>
      <td>31</td>
      <td>3</td>
      <td>1</td>
      <td>Lag Between Second B and A</td>
      <td>4</td>
      <td>False</td>
      <td>7</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>103</th>
      <td>31</td>
      <td>3</td>
      <td>1</td>
      <td>Lag Between Second B and A</td>
      <td>4</td>
      <td>False</td>
      <td>7</td>
      <td>7</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>Lag Between Second B and A</td>
      <td>6</td>
      <td>False</td>
      <td>7</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](Deficient_Encoding_2_files/Deficient_Encoding_2_12_0.png)
    





    0.1969455754894792



### Comparison of Recall Probabilities


    
![png](Deficient_Encoding_2_files/Deficient_Encoding_2_14_0.png)
    


### Lag Distributions by Group


    
![png](Deficient_Encoding_2_files/Deficient_Encoding_2_16_0.png)
    


### Serial Position by Group


    
![png](Deficient_Encoding_2_files/Deficient_Encoding_2_18_0.png)
    


### Subject ID by Group


    
![png](Deficient_Encoding_2_files/Deficient_Encoding_2_20_0.png)
    


### Correlation Analysis




    0.06476299088936412



The greater the lag between a second presentation of B and a second presentation of A, the greater the probability of recalling A. But there's a positive correlation between this second-presentation lag and the lag between presentations of A. So maybe that's just the regular old spacing effect. We aren't effectively controlling for subsequence length yet.

## Results

## <center>Results

### Discussion
Within CMR, a formal model implementing retrieved context theory, a learning rate scalar modulates how strongly items are encoded into memory. The deficient encoding hypothesis calls for a mechanism to be added to CMR that modulates the value of this scalar based on the familarity of the currently encoded item. A hypothetical CMR-DE would thus track for each encoding index a measure of each item's familiarity based on the current state of context. The learning rate for memories of the current item and its contextual associations would then vary inversely with its familiarity.

I attempted to test the deficient encoding hypothesis about repetition effects by focusing on the idea that familiarity might hinge on the contextual dynamics that organize memory according to CMR. Here, the main implication I focus on is the corollary hypothesis that familiarity-based memory impairment for a given item can be increased without necessarily experiencing that item. Instead, contextual states associated with the item from a previous presentation can be reinstated through repetition of items originally presented near said previous presentations that share many of item's contextual associations. 

I found the opposite of the relationship I was looking for, even after trying to control for relevant variables. Unfortunately, even if I did find the expected relationship, these analyses do not do anything to identify an unique role for the deficient processing account of item spacing that contextual variability or study-phase retrieval accounts can't fill. Worse, I think that as long as one conceptualizes deficient processing as something that depends on how retrievable an item is from context, or even just the serial position of the last time an item was encoded, then **in principle any effect on recall connected to deficient processing is just as explicable in terms of the contextual variability account of repetition effects**. So this may be a dead end.

### References
Collins, R. N., Milliken, B., & Jamieson, R. K. (2020). MINERVA-DE: An instance model of the deficient processing theory. Journal of Memory and Language, 115, 104151.

Siegel, L. L., & Kahana, M. J. (2014). A retrieved context account of spacing and repetition effects in free recall. Journal of Experimental Psychology: Learning, Memory, and Cognition, 40(3), 755.
