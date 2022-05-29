# KHIDKI_ms_engage

OVERVIEW OF ALGOS AND COMPARISON

BAG OF WORDS =>
          let n =4			
            word1	word2	word3	word4
		mv tag1	4	      3	    2	   2
		mv tag2	4	      6	    3	   3
		mv tag3	2     	5	    4	   9
		mv tag4	5	      0	    4	   4
      n- dimentional vector space from which we will be taking similar vectors(movies) using cosine similarity
      
  BERT =>       bert is bi-directional so looks at both direction of words that's why it is a more sentence based and that's why it gives sentimental recommendation to based on movie's overview
                
                   
                   
                   collaborative filtering  [drawbacks = cold-start]
           user-based                     item-based (amazon)

                  a user may have some things in common and still likes somethings different
                    that's why item-based > user-based mostly
            
            
            matrix factorisation   we can get  u*m  from      u*k  and k*m   k is common 
matrix factorisation via SVD > gradient descent and  NMF  on the basis of RMSE (error)
            SVD=> Rm∗n = Um∗m Dm∗n Vtn∗n
            
           ![Screenshot 2022-05-29 135242](https://user-images.githubusercontent.com/86410192/170861985-c4b112f7-a7f4-42cf-92db-63a405453cf0.png)


and that's why i build a hybrid of BERT and BAG OF WORDS
