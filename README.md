# TikiTracker
Update: Due to GeekiTiki restructuring their website (as well creating new channels to be updated on their products) this code is now out of date. I will not be updating it but I am leaving it up for future reference.
## Simple script to check a website for updates
#### So whats this all about?
I wanted the ability to see when a webiste added new content without having to check it everyday, which resulted in TikiTracker!
#### How does it work?
First, a Python script gets the html from [GeekiTiki](http://www.geekitikis.com/products) and uses a Regex statement to return all the products inside the list tag. Then after checking if there are any product ID's not in the text file (created the last time it was run), it uses an Apple script to text a picture of the new product to me. All of this is bundled into a Shell script and set as a cron job.
#### Why?
Why not, Python is great for automating things. It also posses an interesting challenge, forcing diffrent scripts to work together. While this example is simple, the idea could be expanded out.
