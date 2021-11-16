# lmu-csmi-3550-locust

I've tested the given "Capitalize" program and the "find Date" program for the second, because the program I wrote for project 2, Blade, requires two users and I haven't find a way to do that with locust yet.

For the Capitalize program, the three tests result are listed in the ./capitalize folder:

  for the first time testing,![image](https://user-images.githubusercontent.com/46990486/141945805-f6886a7b-d934-413e-b7d8-e8e8c09f66be.png)
all of the transferring have failed because I forgot to open the server while testing...
but it is interesting to me on the Error message: "No connection could be made because the target machine actively refused it."

This make me think that the default protocal actually send back a refuse message instead of just dropping the package. Not sure if I'm right though.

In the second test, after opening the server, it started working. What is interesting to me is the request per second chart:
![image](https://user-images.githubusercontent.com/46990486/141946500-24620c77-f69e-4f49-bd63-7729b44b84e8.png)
I wonder why is this request chart not smooth, bucause local host should not have a delay from internet. Is this just how the "long" request and the "short" request distributed?

To look for a similar pattern I took a look at the third test:
![image](https://user-images.githubusercontent.com/46990486/141946837-5fce76f4-b52a-4393-9977-e4eb36ff6f51.png)
But instead, it was way smoother. But then I realized why, and that is because of the scale of the picture. Over all, there is only a +- 0.1 second difference in the second graph. I believe that the stability of the process of sending request and recieving request won't got affected much from the number of request. Or maybe I should try a crazy number.

One more thing intersting on the third chart is the rather high number of request in the very begining on the timeline, for this only happened in the third test. I believe that this difference came from a larger number of users, that all of them are sent in the first seond, but then with the lower rate of requests per second set default by the locustfile that it decreased.



For the Date server one, I did two tests, and the result are in the ./date folder:

![image](https://user-images.githubusercontent.com/46990486/141948449-5c9972df-88bc-4888-a6ff-3fd015720d90.png)
I found that though I did open the server this time, around 15% of the request failed. With the same code but less users I did for test 2, 
![image](https://user-images.githubusercontent.com/46990486/141948868-cd8616e1-fc50-48ee-97ea-482371a68844.png)
the failing percentage went up even higher. Looking at the error messages, there are two kinds:

"An existing connection was forcibly closed by the remote host"

and 

"An established connection was aborted by the software in your host machine"

which comes way more that the former. 

I believe this latter one comes from the reaction time setted by the locustfile, and that I've sent too much requests at the same time for the server to hold. But for the former  one, I am not too sure. I don't think that I've closed the server during the test, and as the graph have shown,
![image](https://user-images.githubusercontent.com/46990486/141949566-19bc3f80-af5e-4d50-9614-d4e6d4388e21.png)
(test 1)
![image](https://user-images.githubusercontent.com/46990486/141949613-3437b8be-59c7-475d-9ba2-fb09939e89ca.png)
(test 2)

that this is a continuous error, and that with this "connection closed" error there are still success messages. This is something I don't understand.
