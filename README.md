# Oakmont

Commenting scheme

When commenting the project please refer to the following requirements for all coding

note these do not need to be followed exactly as the examples describe, they are just examples. Feel free to paraphrase or simplify a bit if you want

1. If you are using a module from another library, refer to what the module is doing
   
eg. #this line gets the html code for the inputed link using the requests module

      requests.get(link)

3. When refering to a module created in another module that we made, note roughly what it does

  eg.
  
     #this method collects price value from the RBA website
      scraper.getRBAInflation()

4. multiple lines that are related to each other can be noted within the same comment, that is fine and works well

eg. 

      #get the consumerIndex and monthlyIndicator values
      consumerIndex = re.search("\d+\.\d+", consumerIndex).group()
      monthlyIndicator = re.search("\d+\.\d+", monthlyIndicator).group()

6. Comment any code that is not clear with its own dedicated line. A line of code is defined unclear if it refers to anything external or is processing inputs.
   eg.

         print('this') 
   the above doesn't require comments
   eg.

         print(testing*graphics)
   the above requires comments as it describes a operation and the base print.
   
8. If possible try and note comments as much as possible to help decribe the process of the program.
   Rule of thumb, over comment is better than under so even if its a simple method or line, commenting is recommended

9. If you have described something previously with comments, you don't need to redescribe the same methods and can simplify
   eg.

         #this method collects price value from the RBA website
         scraper.getRBAInflation()
   And
   
         #get RBA values
         scraper.getRBAInflation()

If you have any issues with what is described above, talk to me (Andrew Still) about it and we can discuss changes.
