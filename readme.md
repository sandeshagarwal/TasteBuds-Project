# Project Title

TasteBuds

## Description

Covered all the required Tasks as required -

Task 1: Recipe CRUD Operations
    a. Create Recipe Endpoint - DONE
    b. Update Recipe Endpoint - DONE
    c. Delete Recipe Endpoint - DONE
    d. Get Recipe Endpoint - DONE

Task 2: Likes and Comments
    a. Allow users to like a recipe - DONE
    Users can like, as well as remove like from a recipe, also created an endpoint to get all the likes on a recipe. Also, when the recipe list or detail endpoint is called we can see likes and comments on that recipe
    b. Allow users to add a comment on a recipe -DONE
    Users can add,modify and delete comment on a recipe, also admin can also modify and delete a user's comment. Also, when the recipe list or detail endpoint is called we can see likes and comments on that recipe.

Task 3:  Docker Compose File
    a. Create a Docker Compose file to define and run the development environment for your
    Recipe Sharing Platform - DONE
    b. Include configurations for the API service, database service, and any other necessary
    services. - DONE

Task 4: User Management and Authorization
    a. Create User Endpoint - DONE
    b. Delete User Endpoint - DONE
    c. Authentication and Authorization
        1. Allowed only admin users can create or delete other users. - DONE
        2. Only admin users or the user who created the recipe can update or delete a recipe.DONE
        3. Every logged in user can add likes and comments. - DONE

Bonus Tasks
    a. Implement ‘Get All Recipes’ endpoint which allows users to fetch all recipes. - DONE
    b.  Include pagination for getting all recipes endpoint. - DONE


## Getting Started

### Dependencies

Dependencies are listed in requirements.txt

### Installing and Executing program

* run the following commands
docker-compose build
docker-compose up -d
* Once, the django container is running, open the container go to exec and run 
python manage.py createsuperuser
* add the details and create a user 
* After navigate to http://localhost:8000/admin and sign in 
* Create a token either from the admin portal or using the login api in accounts
* Once the token is generated - Create new users, recipe, likes, comments and play with all the other feature API's :)

