# Oakmont Inflation Prediction application/site

The Oakmont Inflation Calculator is a program that scrapes and calculates data points over a variety of sites to simulate the rate of change for inflation within the Australian Economy. The calculator takes data points over different points in time, storing them within a host database which is then processed for use. The findings are then taken and hosted over a site that demonstrates the findings of the calculator in a clear-to-understand format. 

 

# How it works? 

The calculator works by taking data points from a list of sites; this being price data and inflation statistics regarding different economic sectors within Australia. This data is then added to a database that manages the data and splits it into two tables, the product table (used to define the item) and the price table (used to define the price or values of specific points at specific times).  

Once the data is collected, the individual points of data are grouped with entries of the same item type and used to create an item expenditure class. This class refers to the change of the statistic over time, created by directly measuring its change over time. These items are then weighted and combined to create a subgroup expenditure class representing the change in a specific item type. 

A good example would be bread. This item class would be defined within the subgroup class of baked goods. Bread would make up a certain percentage of this group and be applied as a single number. This is managed for all items within the database for all subgroups, we use the Australian Bureau of Statistics expenditure classes and sub-expenditure classes to help define these groupings and weights. These processed subclasses are weighted again within larger class groupings and used to define larger sectors of the Australian Economy. Finally, these groupings are weighted a final time and combined to create a singular value representing a rate of change for inflation within the Australian Economy. 

All these steps are managed by an automation controller, which when finished processing this statistic sends the result to our website for use. 


# Commenting scheme

When commenting the project please refer to the following requirements for all coding

note these do not need to be followed exactly as the examples describe, they are just examples. Feel free to paraphrase or simplify a bit if you want

1. If you are using a module from another library, refer to what the module is doing
   
eg. 

      #this line gets the html code for the inputed link using the requests module
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
