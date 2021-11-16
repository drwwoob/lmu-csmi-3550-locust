# lmu-csmi-3550-locust

I've tested the given "Capitalize" program and the "find Date" program for the second, because the program I wrote for project 2, Blade, requires two users and I haven't find a way to do that with locust yet.

For the Capitalize program, the three tests result are listed in the "capitalize" folder:

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
