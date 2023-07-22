[06/24/23-11:56] Log Initialized
[06/24/23-11:56] this is something I've been thinking of making for a while now, something that will provide workouts for me to do and then update them as time goes on so I can progress.
[06/24/23-11:57] I would like to implement openAI's API with this so I don't have to import a bunch of information for the excersisesas well
[06/24/23-12:46] Need to make wireframe for this app when I have the chance
[06/24/23-12:46] I wonder if this is something I can turn into a web application that I can run on the aptserver?
[06/24/23-21:10] I would like to find a way to implement timing, and select a workout to perform
[06/24/23-21:11] the system needs to be able to keep track of a failed workout, start, stop workouts for timing
[06/24/23-21:12] I need to take some time to make a wireframe for this, otherwise I'll just have no idea what I'm trying to do
[07/20/23-08:07] I'm wondering if it would be better to have all the sq_lite code just in that one module
[07/20/23-08:07] actually, now that I'm thinking about it maybe not, since it still needs to close cleanly
[07/20/23-10:32] Just learned about textual, going to investigate first
[07/21/23-21:22] I'm trying to think of the proper structure for this app
[07/21/23-21:23] At first I thought it would be a good idea to make the menu screen the main screen
[07/21/23-21:23] Now I'm thinking the workout screen should be the one at the bottom of the stack
[07/21/23-21:23] It should be the main screen and the menu can be the top screen
[07/21/23-21:24]  that way I can push it, and pop it to get the returned workout information
[07/22/23-10:53] moved css stuff to a different file, will figure out how to seperate later
