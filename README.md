<h1><strong>Flix Reviews</strong></h1>
<img src="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/air.png?raw=true">
<h1>Product Description</h1>
<p>My Milestone 3 project for the Code Institute, is a Movie Review site, where registered users can submit a review of their favourite movies.</p>
<p>The project has been deployed to Heroku and can been seen <a href="https://movie-review-ms3.herokuapp.com/">here.</a></p>
<h1>Table of Contents</h1>
<ul>
    <li><a href="#user-experience">User Experience (UX)</a></li>
    <ul>
        <li><a href="#user-stories">User Stories</a></li>
    </ul>
    <li><a href="#design">Design</a></li>
    <ul>
        <li><a href="#colour-scheme">Colour Scheme</a></li>
        <li><a href="#typography">Typography</a></li>
        <li><a href="#imagery">Imagery</a></li>
        <li><a href="#wireframes">Wireframes</a></li>
    </ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#frameworks">Frameworks Used</a></li>
    <li><a href="#dbschema">Database Schema</a></li>
    <li><a href="#testing">Testing</a></li>
        <ul>
            <li><a href="#code-verification">Code Verification</a></li>
            <li><a href="#lighthouse">Lighthouse</a></li>
            <li><a href="#speed-test">Speed Test</a></li>
            <li><a href="#cross-browser">Cross-Browser</a></li>
            <li><a href="#responsive">Responsive Testing</a></li>
            <li><a href="#testing-user-stories">Testing User Stories</a></li>
        </ul>
    <li><a href="#further-testing">Further Testing</a></li>
    <li><a href="#features-to-implement">Features Left To Implement</a></li>
    <li><a href="#bugs">Bugs</a></li>
    <li><a href="#deployment">Deployment</a></li>
        <ul>
            <li><a href="#heroku">Heroku</a></li>
            <li><a href="#forking-repo">Forking the GitHub Repository</a></li>
            <li><a href="#making-local-clone">Making a Local Clone</a></li>
        </ul>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#code">Code</a></li>
    <li><a href="#content">Content</a></li>
    <li><a href="#media">Media</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
</ul>

<h2 id="user-experience">User Experience (UX)</h2>
<ul>
    <li id="user-stories">User Stories</li>
        <ul>
            <li id="ft-visitor">First Time Visitor Goals</li>
                <ol type="a">
                    <li>As a First Time Visitor, I want to see which movies people rate highly.</li>
                    <li>As a First Time Visitor, I want to read reviews about movies I have not seen.</li>
                    <li>As a First Time Visitor, I want to create an account and submit my own review.</li>
                </ol>
            <li id="returning-visitor">Returning Visitor Goals</li>
                <ol type="a">
                    <li>As a Returning Visitor, I want to see if others have reviewed the same movie.</li>
                    <li>As a Returning Visitor, I want to see which movies people are rating the highest.</li>
                </ol>                       
        </ul>
    <li id="design">Design</li>
        <ul>
            <li id="colour-scheme">Colour Scheme</li>
                <ul>
                    <li>I tried the theme the site like Netflix. The background image and carousel helped me achieve this.</li>                         
                </ul>
            <li id ="typography">Typography</li>
                <ul>
                    <li>The Poppins font is the main font used throughout this project with Sans-Serif as the fallback in case for any reason the font isn't being imported into the site correctly.</li>
                </ul>
            <li id="imagery">Imagery</li>
                <ul>
                    <li>Most of the images used in this site are input by a registered user. Upon creating a review, the user is asked to input the URL to their chosen image. Once the review has been submitted, the image will appear in the Home page carousel.</li>
                </ul>
            <li id="wireframes">Wireframes</li>
                <ul>
                    <li>Project Wireframe - <a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/docs/wireframes.pdf">View</a></li>
                </ul>
            </li>
        </ul>
    <li id="target-audience">Target Audience</li>
        <ul>
            <li>Users of all ages.</li>
            <li>Movie fans.</li>
            <li>Movie critics.</li>
        </ul>
    </li>
</ul>
<h2 id="features">Features</h2>
<ul>
    <li>Responsive on all device sizes.</li>
    <li>Interactivity for users.</li>
    <li>Carousel on loop.</li>
    <li>Users can create an account and leave their own movie review.
    <li>Users can edit or delete their own reviews.</li>
    <li>Ability to read reviews left by other registered users.</li>
    <li>Ability to edit Profile page details.</li>
</ul>
<h2 id="technologies-used">Technologies Used</h2>
<h3>Languages Used</h3>
<ul>
    <li>HTML5</li>
    <li>CSS3</li>
    <li>JavaScript</li>
    <li>Python</li>
</ul>
<h3 id="frameworks">Frameworks, Libraries & Programs Used</h3>
<ol>
    <li><a href="https://getbootstrap.com/docs/4.3/getting-started/download/">Bootstrap 4</a></li>
        <ul>
            <li>Bootstrap was used to assist with the responsiveness and styling of the website.</li>
        </ul>
    <li><a href="https://flask.palletsprojects.com/en/2.0.x/">Flask</a></li>
        <ul>
            <li>Backend Python micro-framework.</li>
        </ul>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
        <ul>
            <li>NoSQL database that is used to store data.</li>
        </ul>
    <li><a href="https://fonts.google.com/">Google Fonts</a></li>
        <ul>
            <li>Google Fonts was used to import the 'Poppins' font into my project.</li>
        </ul>
    <li><a href="https://fontawesome.com/">Font Awesome</a></li>
        <ul>
            <li>Font Awesome was used for the star rating widget.</li>
        </ul>
    <li><a href="https://jquery.com/">jQuery</a></li>
        <ul>
            <li>jQuery is a dependency of the Bootstrap framework and helps with responsive design.</li>
        </ul>
    <li><a href="https://owlcarousel2.github.io/OwlCarousel2/">Owl-Carousel</a></li>
        <ul>
            <li>Used to create a touch enabled, responsive carousel slider.</li>
        </ul>
    <li><a href="https://code.visualstudio.com/">VS Code</a></li>
        <ul>
            <li>The Code Editor used for this project.</li>
        </ul>
    <li><a href="https://git-scm.com/">Git</a></li>
        <ul>
            <li>Git was used for version control.</li>  
        </ul>
    <li><a href="https://github.com/">GitHub</a></li>
        <ul>
            <li>GitHub is used to store the projects code after being pushed from Git.</li>
        </ul>
    <li><a href="https://desktop.github.com/">GitHub Desktop</a></li>
        <ul>
            <li>Used to commit and push changes to GitHub.</li>
        </ul>
    <li><a href="https://balsamiq.com/">Balsamiq</a></li>
        <ul>
            <li>Balsamiq was used to create the wireframes during the design process.</li>
        </ul>
    <li><a href="https://developer.chrome.com/docs/devtools/">Chrome DevTools</a></li>
        <ul>
            <li>Essential tools for debugging code.</li>
        </ul>
</ol>
<h3 id="dbschema">Database Schema</h3>
<p>The MongoDB consists of two collections. 'Users' and 'Reviews'. A visual representation of the database can be seen below.</p>
<img src="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/dbschema.png?raw=true">
<h2 id="testing">Testing</h2>
<h3 id="code-verification">Code Verification</h3>
<p>The W3C HTML Validator, W3C CSS Validator,JSHint and ExtendsClass services were used to validate code to ensure there were no syntax errors in the project.</p>
<ul>
    <li>W3C HTML Validator - <a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/docs/w3c_html.pdf">Results</a></li>
    <li>W3C CSS Validator - <a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/docs/w3c_css.pdf">Results</a></li>
    <li>JSHint - <a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/docs/jshint.pdf">Results</a></li>
    <li>Python Validator - <a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/docs/pythonvalidator.pdf">Results</a></li>
</ul>
<h3 id="lighthouse">Lighthouse</h3>
<p>Performance of the site was analysed by <a href="https://developers.google.com/web/tools/lighthouse">Lighthouse</a>. Here are the results.</p>
<img src="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/lighthouse.png?raw=true">
<h3 id="speed-test">Speed Test</h3>
<p>Site speed test was performed by <a href="https://gtmetrix.com/">GTMetrix</a>. Here are the results.</p>
<img src="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/speedtest.png?raw=true">
<h3 id="cross-browser">Cross Browser Testing</h3>
<p>This project was tested with all major browsers and displayed as expected. Results can be seen here.</p>
<ul>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/chrome.png">Google Chrome</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/firefox.png">Firefox</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/safari.png">Safari</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/opera.png">Opera</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/edge.png">Microsoft Edge</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/tor.png">Tor</a></li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/ie11.png">IE11</a></li>
</ul>
<h3 id="responsive">Responsive Testing</h3>
<p>Responsive testing was carried out with Chrome Dev Tools. The results for some popular devices can be seen below.</p>
<ul>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/galaxyfold.png">Galaxy Fold</a>(280px)</li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/iphonese.png">iPhone SE</a>(320px)</li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/iphonex.png">iPhone X</a>(375px)</li>  
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/pixel2xl.png">Pixel 2 XL</a>(411px)</li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/surfaceduo.png">Surface Duo</a>(540px)</li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/ipad.png">iPad</a>(768px)</li>
    <li><a href="https://github.com/BYates1289/Flask-Movie-Review-Project-MS3/blob/main/flixreviews/static/img/ipadpro.png">iPad Pro</a>(1024px)</li>   
</ul>
<h3 id="testing-user-stories">Testing User Stories from User Experience (UX) Section</h3>
<ul>
    <li>First Time Visitor Goals</li>
        <ol type="I">
            <li>As a First Time Visitor, I want to see which movies people rate highly.</li>
                <ol type="a">
                    <li>Upon entering the site, users are presented with a carousel which loops through recently added reviews left by registered users. Also, once logged in, you can check out the Reviews page, which will list all the reviews left on the site.</li>
                </ol>
            <li>As a First Time Visitor, I want to read reviews about movies I have not seen.</li>
                <ol type="a">
                    <li>The carousel will loop through all reviews left by registered users. Individual reviews can be read, whether the user is registered or not, by clicking the Read Review button.</li>
                    <li>Once a user is registered, they can view the Reviews page which will display all reviews on a single page.</li>
                </ol>            
        </ol>
    <li>Returning Visitor Goals</li>
        <ol type="I">
            <li>As a Returning Visitor, I want to see if others have reviewed the same movie.</li>
                <ol type="a">
                    <li>Once logged in, the user can check whether anyone else has registered a review on the same movie as them on the Review page.</li>
                </ol>
            <li>As a Returning Visitor, I want to see which movies people are rating the highest.</li>
                <ol type="a">
                    <li>As part of the carousel, the reviewed score is shown also. The carousel is on a loop so each review left on the site will be shown along with the rating given.</li>
                    <li>Each review will display the reviewers rating. The user can check these out on the Review page.</li> 
                </ol>            
        </ol>
</ul>
<h3 id="further-testing">Further Testing</h3>
<ul>
    <li>The application was personally tested on a variety of devices such as Desktop, Laptop, Surface Pro 6, iPad Air 2 & iPhone X.</li>
    <li>All testing was undertaken offline using VS Code in a Python Virtual Environment (venv).</li>
    <li>Family members and friends were asked to navigate the application and leave a review. Everyone who tested, confirmed the site was simple to navigate and to leave a review.</li>
</ul>
<h3 id="features-to-implement">Features Left To Implement</h3>
<ul>
    <li>I would love to implement the <a href="https://www.themoviedb.org/documentation/api">TMDB</a> API so that users can search via the API for their movie review. This would pull the movie posters into the application too.</li>
</ul>
<h2 id="bugs">Bugs</h2>
<p>When building the carousel, I had an <<code>a</code>> as parent to multiple <<code>div</code>>, which worked fine, but failed validation. I did this so that the movie poster and title would be linked to the review. I removed it and stuck with the Read Review button.
<h2 id="deployment">Deployment</h2>
<h3 id="heroku">Heroku</h3>
<p>To deploy this project to Heroku, the following steps were taken...</p>
<ol>
    <li>From the VS Code terminal, I created a requirements.txt and Procfile using the following commands:</li><br>
    <div class="snippet-clipboard-content position-relative"><pre><code>pip3 freeze --local > requirements.txt</pre></code></div>
    <div class="snippet-clipboard-content position-relative"><pre><code>echo web: python run.py > Procfile</pre></code></div>
    <li>I then committed these files to GitHub.</li>
    <li>Next, I logged into my Heroku account and created a new app named "movie-review-ms3".</li>
    <li>I then located the <b>Deploy</b> tab and selected <b>GitHub</b> as the Deployment Method.</li>
    <li>Once I authenticated my GitHub account, I selected my repository.</li>
    <li>Then, I went to <b>Settings</b> and clicked the <b>Reveal Config Vars</b> button.</li>
    <li>I then entered the following information...</li>
    <table>
        <thead>
            <tr>
                <th class="text-align-left"><strong>Key</strong></th>
                <th class="text-align-left"><strong>Value</strong></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="text-align-left">IP</td>
                <td class="text-align-left"><code>0.0.0.0</code></td>
            </tr>
            <tr>
                <td class="text-align-left">PORT</td>
                <td class="text-align-left"><code>5000</code></td>
            </tr>
            <tr>
                <td class="text-align-left">SECRET_KEY</td>
                <td class="text-align-left"><code>&lt;app_secret_key&gt;</code></td>
            </tr>
            <tr>
                <td class="text-align-left">MONGO_URI</td>
                <td class="text-align-left">mongodb+srv://USERNAME:PASSWORD@cluster0.9yvjr.mongodb.net/movie?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE</td>
            </tr>
            <tr>
                <td class="text-align-left">MONGO_DBNAME</td>
                <td class="text-align-left"><code>movie</code></td>
            </tr>
        </tbody>
    </table>
    <li>Next, I went back to the <b>Deploy</b> tab and selected <b>Enable Automatic Deploys</b>.</li>
    <li>I then ensured the "main" branch was selected under Manual Deploy, and clicked the <b>Deploy Branch</b> button.</li>
    <li>Shortly after, I recieved a message informing me that my site had been deployed sucessfully.</li>
</ol>
<h3 id="forking-repo">Forking the GitHub Repository</h3>
<p>By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...</p>
<ol>
    <li>Log in to GitHub and locate the GitHub Repository.</li>
    <li>At the top of the Repository, just above the "Settings" Button on the menu, locate the "Fork" Button.</li>
    <li>You should now have a copy of the original repository in your GitHub account.</li>
</ol>
<h3 id="making-local-clone">Making a Local Clone</h3>
<ol>
    <li>Log in to GitHub and locate the GitHub Repository.</li>
    <li>Under the repository name, click "Clone or download"</li>
    <li>To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.</li>
    <li>Open Git Bash.</li>
    <li>Change the current working directory to the location where you want the cloned directory to be made.</li>
    <li>Type <code>git clone</code>, and then paste the URL you copied in Step 3.</li><br>
    <div class="snippet-clipboard-content position-relative"><pre><code>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY</pre></code></div>
    <li>Press Enter. Your local clone will be created.</li><br>
    <div class="snippet-clipboard-content position-relative">    
    <pre><code>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY    
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.</pre></code></div>
</ol>
<p>Click <a href="https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop">here</a> to retrieve pictures for some of the buttons and more detailed explanations of the above process.</p>
<h2 id="credits">Credits</h2>
<h3 id="code">Code</h3>
<ul>
    <li>Bootstrap 4: Bootstrap Library used throughout the project to make site responsive.</li>
    <li>Owl-Carousel for the touch enabled, responsive carousel.</li>
</ul>
<h3 id="content">Content</h3>
<ul>
    <li>All content was written by the developer.</li>
</ul>
<h3 id="media">Media</h3>
<ul>
    <li>The Logo was downloaded from <a href="https://imgbin.com/png/rNVQ4Ea6/popcorn-png">https://imgbin.com/</a></li>
    <li>The background image was downloaded from <a href="https://www.microsoft.com/en-gb/p/netflix/9wzdncrfj3tj?activetab=pivot:overviewtab">Neflix - Microsoft Store.</a></li>
</ul>
<h3 id="acknowledgements">Acknowledgements</h3>
<ul>
    <li>My work colleagues at <a href="https://www.sgworld.com/">SG World</a>, for their insightful feedback/pointers and also for my paid subscription to <a href="https://www.pluralsight.com/">Pluralsight</a>.
    <li><a href="https://codeinstitute.net/">Code Institute</a>, <a href="https://www.pluralsight.com/">Pluralsight</a>, <a href="https://www.udemy.com/">Udemy</a> and <a href="https://youtube.com">YouTube</a> for their extremely good course materials.</li>
    <li>The wonderfully helpful <a href="https://codeinstitute.net/">Code Institute</a> Slack community.
</ul>