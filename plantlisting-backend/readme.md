#  __________________________Plant Listing Project__________________________




## 1. Dashboard


###    1.1 :  For View the Plants Post :
     
- Method : GET
- Request URL : http://127.0.0.1:8000/plant/plant-view/
- Response :  
>            "success": "true",
>            "status code": 200,
>             "data" :
                   {
                        "id": 10,
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "owner": 1,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1",
                        "datetime": "2020-11-27T05:37:13.078210Z"
                    }


                        
## 2. CUSTOM USER MODEL API's  


### 2.1 : For User Registration :
    
-      Method : POST
-      Request URL : http://127.0.0.1:8000/user/register/
      
-      Body :  
            {
                "email":"prag044@gmail.com",
                "password":"12345",
            }
      
-      Response : 

        {
            "status": "success",
            "status code": 201,
            "response": "User Successfully Created But account is not activated"
        }


                (After Registration user have verify their email)

### 2.2 : For User Login :  ***(user login with 'email' and 'password')***
    
-        Method : POST
-        Request URL : http://127.0.0.1:8000/user/login/
        
-        Body :  
                {
                    "email":"prag044@gmail.com",
                    "password":"12345",
                }
        
-        Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": 
                            {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMiwidXNlcm5hbWUiOiJhc2h1dG9zaHNoYXJtYUBleHRlcm5sYWJzLmNvbSIsImV4cCI6MTYxMDUyMzMzMiwiZW1haWwiOiJhc2h1dG9zaHNoYXJtYUBleHRlcm5sYWJzLmNvbSIsIm9yaWdfaWF0IjoxNjEwMzUwNTMyfQ.dP2pAAWJQHECOGvo0y5On6n3EbgCuDKcF4z1jrRpPNw",
                    "is_varified": true
                            }
            }



### 2.3 : For User Login :  ***(user login with sending OTP on registered 'email')***
    
-        Method : POST
|        ____________USER LOGIN WITH "EMAIL"____________
        
-        Request URL : http://127.0.0.1:8000/user/otp-login/
        
-        Body :  
                {
                    "email":"prag044@gmail.com",
                }
        
-        Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": "otp sent"
                        
            }
                 
|        ____________USER After Gatting OTP on "EMAIL"____________

-        Body :  
                {
                    "email":"prag044@gmail.com",
                    "otp":988697
                }
        
-        Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": 
                                           {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMiwidXNlcm5hbWUiOiJhc2h1dG9zaHNoYXJtYUBleHRlcm5sYWJzLmNvbSIsImV4cCI6MTYxMDUyMzMzMiwiZW1haWwiOiJhc2h1dG9zaHNoYXJtYUBleHRlcm5sYWJzLmNvbSIsIm9yaWdfaWF0IjoxNjEwMzUwNTMyfQ.dP2pAAWJQHECOGvo0y5On6n3EbgCuDKcF4z1jrRpPNw",
                    "is_varified": true
                            }
                
                        
            }

 
    
### 2.4 : For Update User Profile :

-        Method : GET
-        Request URL : http://127.0.0.1:8000/user/profile/
        
-        Body :  
                
                                      !!.................Token Required.......................!! 
                    
        
-        Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": 
                        {
                            "username": "ashutosh",
                            "first_name": "ashutosh",
                            "last_name": "sharma",
                            "phone_number": "9660222632",
                            "address": "delhi"
                        }
                    
            }
   


-        Method : PUT
-       Request URL : http://127.0.0.1:8000/user/updateprofile/6/
        
-      Body :  
                
             !!.................Token Required.......................!!

                   {
                            "username": "ashutosh",
                            "first_name": "ashutosh",
                            "last_name": "sharma",
                            "phone_number": "9660222632",
                            "address": "delhi"
                   }    
                    
        
 -       Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": 
                   {
                            "username": "ashutosh",
                            "first_name": "ashutosh",
                            "last_name": "sharma",
                            "phone_number": "9660222632",
                            "address": "delhi"
                   }
                    
            }


### 2.5 For Update User Password :
    

-            Method : PUT
-            Request URL : http://127.0.0.1:8000/user/updatepassword/


-        Body :  
                
             !!.................Token Required.......................!!

                    {
                        "old_password": "12345",
                        "new_password1": "extern@9660"
                        "new_password2": "extern@9660"
                        
                    }
                    
        
-        Response : 

            {
                "status": "success",
                "status code": 204 No_Contant,
                "response": 
                    {
                        "sucess":"password updated Successfully"
                    }
                    
            }

### 2.5 For Forgot User Password :
    

-            Method : POST
-            Request URL : http://127.0.0.1:8000/user/forgot-password/


-        Body :  

                    {
                        "email":"ashuhardaska26@gmail.com"
                        
                    }
                    
        
-        Response : 

            {
                "status": "success",
                "status code": 200 OK,
            }


-            Method : POST
-            Request URL : http://127.0.0.1:8000/user/token/<str:token_data>/


-        Body :  

                    {
                        "new_password":"88888",
                        "confirm_new_password":"565565"
                        
                    }
                    
        
-        Response : 

            {
                "status": "success",
                "status code": 200 OK,
                "response":
                {
                    "Update Sucessfully"
                }
            }

## 3. Plnats_Model API's  
    

### 3.1 : For Post the Plant :
    
-      Method : POST
-      Request URL : http://127.0.0.1:8000/plant/plantpost/

-      Body :  
                
             !!.................Token Required.......................!!

                    {
                        "plant_name": "test1",
                        "plant_type":1,
                        "description":"this is a banana plant",
                        "quantity": 15,
                        "img1": [],
                        
                    }
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "data" : 
                   {
                        "id": 10,
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "owner": 1,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1",
                        "datetime": "2020-11-27T05:37:13.078210Z"
                    }



### 3.2 : For GET / Update / Delete the Plant :



-      Method : GET 
      
-      Request URL : http://127.0.0.1:8000/plant/updateplant/10/

-      Body :  
                
             !!.................Token Required.......................!!

                
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "data" : 
                    {
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }

    
      
-      Method : PUT (_____________________FOR UPDATE__________________)
      
-      Request URL : http://127.0.0.1:8000/plant/updateplant/7/

-      Body :  
                
             !!.................Token Required.......................!!

                    {
                        "plant_name": "Newtest1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "data" : 
                    {
                        "plant_name": "Newtest1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }

      
      
-      Method : Delete (_____________________FOR Delete _________________________)

      
-      Request URL : http://127.0.0.1:8000/plant/updateplant/10/

-      Body :  
                
             !!.................Token Required.......................!!

-      Response :  
            "success": "true",
            "status code": 200_OK,


### 3.3 : For User Contact :



-      Method : GET 
      
-      Request URL : http://127.0.0.1:8000/plant/usercontactview/1/

-      Body :  
                
             !!.................Token Required.......................!!

                
-      Response :  
            "success": "true",
            "status code": 200 Ok,
            "data" : 
                        {
                            "first_name": "ASHUTOSH",
                            "last_name": "SHARMA",
                            "phone_number": "********",
                            "address": "JAIPUR"
                        }


### 3.3 : For GET Plant Post By User :



-      Method : GET 
      
-      Request URL : http://127.0.0.1:8000/plant/userplants/

-      Body :  
                
             !!.................Token Required.......................!!

                
-      Response :  
            "success": "true",
            "status code": 200 Ok,
            "data" : 
                    [
                        {
                            "id": 10,
                            "plant_name": "test1",
                            "plant_type": [],
                            "other_p_type": null,
                            "description": "this is a description of test plant",
                            "quantity": 15,
                            "owner": 1,
                            "img1": /media/download_4iICanr.jpeg,
                            "img2": [],
                            "img3": [],
                            "img4": [],
                            "status": "1",
                            "datetime": "2020-11-27T05:37:13.078210Z"
                        },
                        {
                            "id": 3,
                            "plant_name": "sunflower2",
                            "plant_type": [
                                1
                            ],
                            "other_p_type": null,
                            "description": "This is sun flower",
                            "quantity": null,
                            "owner": 1,
                            "img1": /media/download_4iICanr.jpeg,
                            "img2": [],
                            "img3": [],
                            "img4": [],
                            "status": "1",
                            "datetime": "2020-11-10T06:04:35.703772Z"
                        },
                        {
                            "id": 1,
                            "plant_name": "Rose",
                            "plant_type": [
                                1,
                                2
                            ],
                            "other_p_type": null,
                            "description": "This is a rose plant",
                            "quantity": 6,
                            "owner": 1,
                            "img1": /media/download_4iICanr.jpeg,
                            "img2": [],
                            "img3": [],
                            "img4": [],
                            "status": "1",
                            "datetime": "2020-11-19T04:49:02.036595Z"
                        }
                    ]

            
### 3.4 Api's For WishList :- 

-      Method : POST 
      
-      Request URL : http://127.0.0.1:8000/plant/wishlist/

-      Body :  
                
             !!.................Token Required.......................!!

                    {
                        "plant_id": "1"
                    }
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "data" : 
                        {
                            "id": 14,
                            "add_date": "2020-12-01T04:20:44.277066Z",
                            "user_id": 2,
                            "plant_id": 8
                        }

-      Method : GET 
      
-      Request URL : http://127.0.0.1:8000/plant/wishlistview/

-      Body :  
                
             !!.................Token Required.......................!!

-      Response :  
            "success": "true",
            "status code": 200 OK,
            "data" : 
                    [
                        {
                            "id": 10,
                            "add_date": "2020-12-01T04:20:08.247641Z",
                            "user_id": 3,
                            "plant_id": 5
                        },
                        {
                            "id": 11,
                            "add_date": "2020-12-01T04:20:14.501265Z",
                            "user_id": 3,
                            "plant_id": 8
                        }
                    ]

-      Method : DELETE 
      
-      Request URL : http://127.0.0.1:8000/plant/wishlistview/1/

-      Body :  
                
             !!.................Token Required.......................!!

      Response : 

        {
            "status": "success",
            "status code": 200_ok ,
            "Response" : "User Deleted Successfully"
           
        }
    

## 4. Admin User Model API's : 


###  4.3 :   For GET all User By Admin :
   

-      Method : GET
-      Request URL : http://127.0.0.1:8000/user/users/
      

-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------- 
      
      
      Response : 

        {
            "status": "success",
            "status code": 200 ok,
            "response": 
                    [
                        {
                                "id": 2,
                                "password": "pbkdf2_sha256$180000$xKKZPH7rX5g7$jR29/Djbsbznvdi8kQHDoEXg7sZjpVe/pGg3IC0odVw=",
                                "last_login": "2020-11-24T10:20:18.330598Z",
                                "is_superuser": false,
                                "username": "gaurav",
                                "first_name": "gaurav",
                                "last_name": "surolia",
                                "is_staff": false,
                                "is_active": true,
                                "date_joined": "2020-11-10T06:01:10Z",
                                "email": "gaurav@gmail.com",
                                "phone_number": "861919895",
                                "address": "jaipur",
                                "groups": [],
                                "user_permissions": []
                            },
                            {
                                "id": 3,
                                "password": "pbkdf2_sha256$180000$nCbnmKC3U6hj$KJQPZUWOspuRuMOKWA/NgS7NG0uYTptdxrA6rWhEDOw=",
                                "last_login": "2020-11-19T10:36:15.086974Z",
                                "is_superuser": false,
                                "username": "ashu",
                                "first_name": "ashu",
                                "last_name": "tosh",
                                "is_staff": false,
                                "is_active": true,
                                "date_joined": "2020-11-18T05:48:04Z",
                                "email": "ashu@gmail.com",
                                "phone_number": "9826269798",
                                "address": "jaipur",
                                "groups": [],
                                "user_permissions": []
                            },
                    
                       
                    ]
        



### 4.4 :    For User UPDATE / DELETE BY ADMIN :
    

-      Method : PUT  (_____________________FOR UPDATE__________________)

-      Request URL : http://127.0.0.1:8000/user/updateprofile/1/
      

-      ----------------- Note :- Admin User Login Required ------------------ 
      

      Body :  
                {
                    "username": "ashu",
                    "first_name": "ashu",
                    "last_name": "tosh",
                    "phone_number": "9826269798",
                    "address": "jaipur"
                }
      
-      Response : 

        {
            "status": "success",
            "status code": 200 ok ,
            "response": 

                    {
                        "username": "ashu",
                        "first_name": "ashu",
                        "last_name": "tosh",
                        "phone_number": "9866577852",
                        "address": "delhi"
                    }
        }



-      Method : DELETE  (_____________________FOR DELETE__________________)

-      Request URL : http://127.0.0.1:8000/user/updateprofile/1/
      

-     ------------------------------------- Admin User Login Required !!!  --------------------------------------------  
      
      Response : 

        {
            "status": "success",
            "status code": 200_ok ,
            "Response" : "User Deleted Successfully"
           
        }



###  4.6 :   For GET / Update / Delete the Plants :
    

-      Method : GET (_____________________FOR GET__________________)
      
-      Request URL : http://127.0.0.1:8000/plant/updateplant/10/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------  


      Response :  
            "success": "true",
            "status code": 200 OK,
            "data" : 
                    {
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }
      

-      Method : PUT (_____________________FOR UPDATE__________________)
      
-      Request URL : http://127.0.0.1:8000/dashboard/admin/plant-detail/7/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------  


      Body :  
                
                    {
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "data" : 
                    {
                        "plant_name": "test1",
                        "plant_type": [],
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1"
                    }

      
      
-      Method : Delete (_____________________FOR Delete _________________________)

      
-     Request URL : http://127.0.0.1:8000/dashboard/admin/plant-detail/7/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------  

-      Response :  
            "success": "true",
            "status code": 200 OK


    
###  4.7 :   For POST plant_type :

-      Method : POST

      
-      Request URL : http://127.0.0.1:8000/plant/plant-type/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------  


      Body :  
                
             

                   {
                       "name" : "vegetable"
             
                    }
-      Response :  
            "success": "true",
            "status code": 201 Created,
            "response" : 
                            {
                                "id" : "1"
                                "name": "vegetable"
                            }


        
###  4.8 :   For GET / UPDATE / DELETE Plant Type :

-        Method : GET 

-        Request URL : http://127.0.0.1:8000/plant/plant-type/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------


        Response : 
            "success" : true,
            "status code" : 200 ok,
            "response" : 
                    [
                        {
                            "name": "Flower"
                        },
                        {
                            "name": "Grass"
                        },
                        {
                            "name": "vegetable"
                        }
                    ]



-        Method : UPDATE 

-        Request URL : http://127.0.0.1:8000/plant/plant-type/3/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------


        Response : 
            "success" : true,
            "status code" : 200 ok,
            "response" : 
                    
                        
                        {
                            "name": "fruits"
                        }
                    

        
        
-        Method : DELETE 

-        Request URL : http://127.0.0.1:8000/plant/plant-type/3/


-      ------------------------------------- Admin User Login Required !!!  --------------------------------------------


        Response : 
            "success" : true,
            "status code" : 200 OK,
       









## 5. For Chat in Plant Listing 
 
    

-    Request URL : http://127.0.0.1:8000/chat/chats/
        
         (Login user in DB and Select the user  for chat)

-    Redirect URL : http://127.0.0.1:8000/chat/<username>/


## 6 : For User Login/Registration With (Google/Facebook) :

#### 6.1  Through Google
    
-      Method : POST
-      Request URL : http://127.0.0.1:8000/user/google/
      
-      Body :  
            {
                access_token:"______Google access token________"
            }
      
-      Response : 

        {
            "status": "success",
            "status code": 200,
            "response": "___________________Jwt________Token_______________"
        }


#### 6.1  Through Facebook
    
-      Method : POST
-      Request URL : http://127.0.0.1:8000/user/facebook/
      
-      Body :  
            {
                access_token:"______Google access token________"
                email: "__email___"
                url: "____url ____"
                auth_provider : "___graphDomain__"

            }
      
-      Response : 

        {
            "status": "success",
            "status code": 200,
            "response": "___________________Jwt________Token_______________"
        }



## 7 : For Newsletter :

-      Method : POST
-      Request URL : http://127.0.0.1:8000/user/subscribe/
      
-      Body :  
            {
               
                email: "123@gmail.com"
                

            }
      
-      Response : 

        {
            "status": "success",
            "status code": 200,
            "response": 'message':'thanks for subscribe'
        }

    
## 8 : For filter plants :

-      Method : GET
-      Request URL : http://127.0.0.1:8000/plant/filter/
      
      [search by plant_name = test1 and plant_type = flower]
      plant-types/
-      Response : 

                   {
                        "id": 10,
                        "plant_name": "test1",
                        "plant_type": flower,
                        "other_p_type": null,
                        "description": "this is a description of test plant",
                        "quantity": 15,
                        "owner": 1,
                        "img1": /media/download_4iICanr.jpeg,
                        "img2": [],
                        "img3": [],
                        "img4": [],
                        "status": "1",
                        "datetime": "2020-11-27T05:37:13.078210Z"
                    }


## 9 : For View plant-type:

-      Method : GET
-      Request URL : http://127.0.0.1:8000/plant/plant-types/
      
      
-      Response : 

                   {
                        "id": 10,
                        "plant_type": flower,
                    },

                    {
                        "id": 11,
                        "plant_type": grass,
                    }

## 10 : For User Account-Activation Button :  
    
-        Method : POST
|                   ____________USER LOGIN WITH "EMAIL"____________
        
-        Request URL : http://127.0.0.1:8000/user/account-activation/
        
-        Body :  

            !!.................Token Required.......................!!
        
-        Response : 

            {
                "status": "success",
                "status code": 200 ok,
                "response": "___Activation_url_send_____"
                        
            }

 
