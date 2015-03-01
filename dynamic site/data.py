class PageData(object):
    def __init__(self):
        self.header = """<header>
<img id="Logo" src="Images/Neil_Lane_Logo.svg" alt="Neil Lane Logo"/>
<nav>
<a href="?title=Welcome">Home</a>
<a href="?title=Results">Results</a>
<a href="?title=Details">Details</a>
<a href="?title=Favorites">Favorites</a>
<a href="?title=Login">Login</a>
<a href="?title=Sign Up">Sign Up</a>
</nav>
</header>"""
        self.home = """<section>
<h1 id="huge">
Find the best cameras with <br/>Neil Lane
</h1>
<form action="?title=Results">
<input type="search"/>
<button type="submit">
Search Now!
</button>
</form>
</section>""" #index.html
        self.results = """<section class="white" id="results">
<form  action="?title=Results"><input type="text" /></form>
<div class="results">
<a href="?title=Details">
<img src="Images/Leica.png" alt="Leica Camera"/>
<p>Leica MP .72 Rangefinder Film Camera, Black</p>
</a>
</div>

<div class="results">
<a href="?title=Details">
<img src="Images/Fujifilm.png" alt="Fujifilm Camera"/>
<p>Fujifilm GF670 Professional Camera with Lens</p>
</a>
</div>

<div class="results">
<a href="?title=Details">
<img src="Images/Horseman.png" alt="Horseman Camera"/>
<p>Horseman SW-612 Pro Medium Format Panorama Camera with 65mm Grandagon-N Lens</p>
</a>
</div>

<div class="results">
<a href="?title=Details">
<img src="Images/Toyo.png" alt="Toyo Camera"/>
<p>Toyo 45CF Field Camera</p>
</a>
</div>

<div class="results">
<a href="?title=Details">
<img src="Images/Nikon.png" alt="Nikon Camera"/>
<p>Nikon FM-10 Body with 35-70 f/3.5-4.8 and Black and White Filters</p>
</a>
</div>

</section>""" #results.html
        self.details = """<section class="white" id="details">
<img src="Images/Leica_Large.png" alt="Leica Camera"/>
<h2>Leica MP .72 Rangefinder Film Camera, Black</h2>
Item: LC4916   Mfr: 10302
<br/>
By Leica
<form action="?title=Favorites"><button>Add to favorites</button></form>
<br/>
This product hasn't been rated yet. <a href="?title=Login">Write a Review</a>
<br/>
$ 4,995.00
</section>""" #details.html
        self.favorites = """<section class="white" id="favorites">
<h1>Favorites</h1>
<a href="?title=Details">
<img src="Images/Leica.png" alt="Leica Camera"/>
<p>Leica MP .72 Rangefinder Film Camera, Black</p>
</a>
</section>""" #favorites.html
        self.login = """<section class="white" id="login">
<h1>Login</h1>
<form>
<input type="email" placeholder="email"/>
<br/>
<input type="password" placeholder="password"/>
<br/>
<button type="submit">Submit</button>
</form>
<aside>
<a href="?title=Sign Up">Sign up</a>
</aside>
</section>""" #login.html
        self.signup = """<section class="white">
<h1>Sign Up</h1>
<form>
<input type="email" placeholder="email"/>
<br/>
<input type="password" placeholder="password"/>
<br/>
<input type="password" placeholder="confirm password"/>
<br/>
<button type="submit">Submit</button>
</form>
</section>""" #signup.html