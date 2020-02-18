# WallChanger
A wallpaper changer app using UnSplash API for linux.

# To use the app:
1. Get API key from UnSplash : https://api.unsplash.com/
2. git clone this repository
3. Make edits indicated in source code
4. Execute python script using python3 
5. Just like that a new wallpaper is installed on your machine!

# Here's how the app works:

1. On execute
  
2. Retrieves Background Img Link <br>
    a. Call UnSplash API URL : 'https://api.unsplash.com/search/photos?           page='+PAGE_NUM+'&query='+QUERY_TERM+'&client_id='+self.client_id <br>
    b. Extract Randomly Picked Img Link 

3. Downloads Img using Img Link <br>
    a. Using subprocess python library <br>
    &nbsp;i. Uses "curl -o filename IMG_URL" to download image <br>
    b. Using gio python library <br>
    &nbsp;i. Sets background image
