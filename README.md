# Step for setup the Bakery_management Application

Step 1. Install python(V3.9), django(V3.1.6) and djnago restframework(V3.12.2).
        
        pip install djangorestframework
        
Step 2. Update your SECRET_KEY in config.py file.
        
        Step 2. Update your SECRET_KEY in config.py file.

     By default it has sqlite3 but you want to use Mysql or anyother database, then remove sqlite3 config settings from setting.py file and update the                  required server configuration in Config.py file as eg given for mysql in comments
   
Step 3. Now, we are done with the pre-requisites. Run the migration command to create the tables schema by the commands as given below.

    1. python3 manage.py makemigrations
    2. python3 manage.py migrate
   
Step 4. Create super User:

    1. python3 manage.py createsuperuser
  
Step 5. Run the server.

    python3 manage.py runserver
    
Step 6. Add the Ingredient  using addIngredient API via POSTMAN or django server. request POST : http://127.0.0.1:8000/ingredient/

   Example request body given below,update the content in <> with the real content, and provide the admin credential in Authorisation ( **Use basic Auth** )
     
     BODY :   {

          "name": "<Ingredient_name>"
         
      }
          
step 7. Get the Ingredient List by using Ingredient api request GET:    http://127.0.0.1:8000/ingredient/
        In response you get list of Ingredients
       
        Response:-       
                [
                    {
                        "id": 1,
                        "name": "milk"
                    },
                    {
                        "id": 2,
                        "name": "water"
                    }]


Step 8. Add the BakeryItem by using bakeryitem API via POSTMAN or django server.request POST : http://127.0.0.1:8000/bakeryitem/

      Example request body given below,update the content in <> with the real content, and provide the admin credential in Authorisation (**Use basic Auth** )
     
           BODY :   {
                        "name": "<bakery_item name>",
                        "cost_price": <cost_price>,
                        "selling_price": <selling_price>,
                        "quantity_inhand": <instock_quantity>,
                        "ingredient_details": [
                            {
                                "ingredient": <ingredient1_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "ingredient": <ingredient2_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "ingredient": <ingredient3_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "ingredient": <ingredient4_id>,
                                "quantity": <quantity_percentage>
                            }
                        ]
                    }
                    
           Response:-  
           {            "id":<id>,
                        "name": "<bakery_item name>",
                        "cost_price": <cost_price>,
                        "selling_price": <selling_price>,
                        "quantity_inhand": <instock_quantity>,
                        "ingredient_details": [
                            {
                                "id":<id>,
                                "ingredient": <ingredient1_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "id":<id>,
                                "ingredient": <ingredient2_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "id":<id>,
                                "ingredient": <ingredient3_id>,
                                "quantity": <quantity_percentage>
                            },
                            {
                                "id":<id>,
                                "ingredient": <ingredient4_id>,
                                "quantity": <quantity_percentage>
                            }
                        ]
                    }
 
step 9. Getting the BakeryItem  list by using bakeryitem API via POSTMAN or django server.request GET http://127.0.0.1:8000/bakeryitem/

         Example request body given below,update the content in <> with the real content, and provide the admin credential in Authorisation (**Use basic Auth** )
   
          Response:- List of bakery item with ingredients details.
    
    
step 10. Update the bakery item and ingredient_details by using bakery bakeryitem API via POSTMAN or django server.request GET http://127.0.0.1:8000/bakeryitem/<bakery_item_id>


    Example request body given below,update the content in <> with the real content, and provide the admin credential in Authorisation (**Use basic Auth** )
      
      Response: Updated bakery_item detail
      
  

step 11. Customer Registration by using registration API via POSTMAN or django server.request POST http://127.0.0.1:8000/registration/
   
   
      Body= {
              "username":"<customer_username>",
              "email":"<customer_emai>",
              "first_name":"<customer_firstname>",
              "last_name":"<customer_lastname>",
              "password":"<password>"
              }
              
      Response:{
      "msg":"registration has been completed successfully"
      
      
step 12: Customer can  view the bakery items by using menu API via POSTMAN or django server.request GET http://127.0.0.1:8000/menu/
       
       Example request body given below,update the content in <> with the real content, and provide the customer credential in Authorisation (**Use basic Auth** )

    Response:-   {
                          "id": 1,
                          "name": "cake",
                          "selling_price": 200,
                          "quantity_inhand": 50,
                          "ingredient_details": [
                              {
                                  "id": 1,
                                  "ingredient": 2,
                                  "quantity": 14
                              },
                              {
                                  "id": 2,
                                  "ingredient": 2,
                                  "quantity": 20
                              }
                          ]
                      }
                    
                    
step 13: Customer can Order the bakery items by using Order Api via POSTMAN or django server.request POST http://127.0.0.1:8000/order/

        Example request body given below,update the content in <> with the real content, and provide the customer credential in Authorisation (**Use basic Auth** )
        Body;- {
                    "order_detail": [
                        {
                            "bakery_item": 1, --------------- bakery item id 
                            "quantity": 1 ------------------- quantity wants to order
                        }
                    ]
                }
          
          Response:-{
                        "user": "<user_firstname>",
                        "Total_amount": <Total amount>,
                        "order_date": "<order_date>",
                        "order_detail": [
                            {
                                "bakery_item": <bakery_item_id>,
                                "quantity": <quantity_order>,
                                "amount": <total price of item>
                            }
                            
                        ]
                    }
          
 step 14: Customer can see their order history by using orderhistory API via POSTMAN or django server.request Get http://127.0.0.1:8000/orderhistory/
 
    Example request body given below,update the content in <> with the real content, and provide the customer credential in Authorisation (**Use basic Auth** )
    
    response : list of order item ordered by themself
    
    
Thank you

    
