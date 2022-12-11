# WODASOFT

## Setup
Run file setup.sh to make setup

## Django i18n support
 1. In databse there is a model created as **Transalation** in **language** app to store JSON field.
 2. **LANGUAGES** is the variable stored in setting.py in which all languages are declared.


<br>

## Trees

Here suggested 3 ways to store the data like tree in RDBMS

  1. ### Storing Parent and child - 
       - #### Pros - 
          - Here for each node parent as well left and right child id is stored.
          - As left and right child are stored its easy to get any desired sides child.
          - As parent node is stored we are directly query for parent node value and get both childs.
          - As parent node is directly connected its easy to find relation to parent and its parent and so on
        - #### Cons -
          - We are storing extra node of parent to track parent.
          - Only two child relation is easy to mention.

   2. ### Storing only Child - 
      - #### Pros -
        - Here for each node left child and right chld is stored.
        - As left and right child are stored its easy to get any desired sides child.
        - We can get child count directly going through connected childs.
       - #### Cons -
         - As parent id is not stored its hard to go to make relation to the parent.
         - Only two child relation is easy to mention.


   3. ### Storing only Parent -  
      - #### Pros -
        - Less storage is required as no child id is stored.
        -  As parent node is stored we are directly query for parent node value and get all childs.
        - As parent node is directly connected its easy to find relation to parent and its parent and so on.
        - Many childs can be stored.
       - #### Cons -
         - As childs are not directly connected so hard to track childs.