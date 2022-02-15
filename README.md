# CS50W Project 2 - Commerce
Project 3/6 for CS50W
> Status:submitted
  
### Description
* An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”
* Languages used are HTML, CSS and Python. Django is used as web framework and SQLite as the database.
  
### Contents:
#### Models
There are 6 models/tables in this project which are:
* User, for storing data about the user and whether or not they are an admin.
* Lists, for storing data about all of the lists that have been made.
* Bids, which contains the bidded price for a list and whoever have placed the bid.
* Comments, for storing all the comments that have been made on a list.
* Watchlist, for storing all the lists that a user has put on their watchlist.
* ListDump, for storing all of the auctions that a user has won.

#### Create listing
* Users are able to visit a page to create a new listing. 
* They are also able to specify a title for the listing, a text-based description, and what the starting bid should be. 
* Users also optionally have the ability to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, etc.).

#### Active listings page
* The default route of this web application is the active listings page where a user can see all of the currently active listings.
* Each listing also displays the title, description, current price, and photo (if one exists for the listing) of the list.

#### Listing page
* When a user clicks on any of the active listings, they are redirected to a page displaying information about that specific listing.
* The information contains:
    * Title, image (if one exists for the listing), current price, the user who created the listing and category for that listing.
    * Signed in users are able to place their bid for that listing and also place the listing on their watchlist.
    * If a user tries to place a bid that is lower than or equal to the current bid, they will be presented with an error.
    * Signed in users are also able to post their comments about that listing.
    * If a user is checking their own listing, they are able to close the auction, making the user who placed the highest bid win the auction and the listing will no longer be active.

#### Watchlist
* Users who are signed in are able to view all of the items that they have put on their watchlist.

#### Categories
* When going to the categories page, users are shown all of the current categories that are available.
* Clicking either one of the categories will redirect a user to a page where they can see all of the active listings that are under that category.

#### Django admin interface
* Admins have access to Django's admin interface where they can view, add, edit or delete any lists, bids or comments that have been made in the web application.
  
### Acknowledgements
Really grateful to these other resources (besides the [django docs](https://docs.djangoproject.com/en/4.0/) and [stack overflow](https://stackoverflow.com/)) for helping me out with this project:
* [Fetch Data From a Database And Output To A Webpage by Codemy.com](https://www.youtube.com/watch?v=H3joYTIRqKk)
* [Bootstrap card documentation](https://getbootstrap.com/docs/4.1/components/card/)

### About CS50W
CS50W is a continuation of [CS50](https://cs50.harvard.edu/), diving more deeply into the design and implementaion of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap. Topics include database design, scalability, security, and user experience.  
> Want to learn CS50W for **free**? You can check out their OpenCourseWare [here](https://cs50.harvard.edu/web/).
  
### Note on academic honesty
If you're taking CS50W, either through [Harvard Extension School](https://extension.harvard.edu/), [Harvard Summer School](https://summer.harvard.edu/) or [OpenCourseWare](https://cs50.harvard.edu/web/), please do not blindly copy paste my code. You are putting yourself at a huge risk for getting excluded from the course by the staff themselves as they grade each project thoroughly. This is a course offered by Harvard, and you will be put up to their standard.
