---
title: Moss — finance MCP rollout check-in — transcript
meeting: "[[2026-06-29-moss-finance-rollout]]"
created: 2026-06-29
type: transcript
---

Them: Yeah, yeah, yeah.

Me: Good morning moss users. Very good how you guys doing Quincy?

Them: Run using the new admiral pioneer drink bottle. Nice. Good. Yeah, the water. Especially in the heat. Yeah.

Me: This could be a whole half hour or it could be 10 minutes I wanted to check in and see how it's going I believe it's installed. That correct?

Them: Yes, it is. I installed mine this morning. And it seems to be installed. I haven't tested it yet.

Me: Oh should we do a cheeky little live test?

Them: Oh yeah, it's installed. We can do that. Thomas, I just want to let you know, so it is installed on everyone's machine. So Christian, Dave, these two and jades, it's five people. One of the things I noticed on Friday when I was trying to test your solution for Christian around getting out invoices is it was throwing an error and it was saying because of the API key. So it seems like we each need to have our own API key. So I just wanted to throw that out there that is like now we've got it installed, but it seems like the API key. Might be causing an issue. We might each have to have our own. We can only have five. So in all moss this morning and it said we can only have five API keys.

Me: I mean have you all got your own API key just now or you're using the same one.

Them: Some of us have our own. Some have used like I've gone and used while still working. It is okay. Yes. Probably it's a sign that key to you.

Me: Queen.

Them: I feel like it's not my first and then probably the second user who uses my key, my notepad properly. Yeah, so what I can do to test it is try a different key and let's test Annelies version.

Me: I mean why don't we just use the one I was using that worked.

Them: Don't think what Queen's saying is it's not allowing people to use the same one. Is that what you're saying? Because see it's like kicking people off. Yeah, we can all try usual key, Tom, but I think it's kicking people off. Because I think I've used the one I gave you, Tom. Is that the one, the one I email did the email it through to you, the original one?

Me: Yeah. Yeah.

Them: Yeah, that's the one I used this morning to like do my setup. So I think.

Me: What's the error so because this started with like you tried to do the thing you tried to get file I thought you meant it just what was the error that you saw?

Them: A connective. So MCP is working. You can see it in dev running all good. And I have been connected and I have got data before and now I'm saying connection and what API key. So then copy that in asked it what is this? And it's like you can't use it said something along the lines of you can't use the same API key to somebody else. It might have been allocated or something like that.

Me: But it might be wrong.

Them: So it could be wrong. Very likely can be wrong. Just throwing all the information.

Me: So you went around and installed this on people's machines. Did you use the same API key for everybody when you did that?

Them: So Quincy had someone asked you the installation, so I don't know what the thing used a different API key. Christian me have the same API key and at least choose the one you've. Yeah. So we've all got some of same, some don't.

Me: Should we all try and ask for a file or as we will try for some dumber? Or I guess my curse to my question would have been like, did that then not allow you to do anything in moth or was it just about not allowing you to see the invoice?

Them: Do that. Yeah, it's just not letting me get data from us saying that my mcp is timing out and it is the keys. Verify your API keys are still valid in moss. So curious to see if Quincy, because I think we're using the same key, Quincy, if you can get data this morning out of mass. Okay.

Me: So does everyone have like.

Them: Should we all queries something?

Me: Different? Yeah, go on. Does everyone have like these cases?

Them: Should we all query this the same thing? Yeah. Let's ask it to give us a list of expenses. The last expenses done in the last 10 days. I think specific either card transactions or invoices in that. Yes. So give me the last. Five voices from last. Thinking.

Me: In queen cv, use this for anything in the real world yet so far?

Them: But I feed the information in. Like I give it a file downloaded. And then it just creates me, like select messages with the links and.

Me: So you haven't used like you haven't used, you haven't had.

Them: All. It's for approvals.

Me: Sorry, so you haven't used clods to like ask it from mass data yet?

Them: I, well, like when I did it, it didn't give me like the correct information. Like it just said there were no. Expenses or it didn't give the right amount of information.

Me: Can I ask that when you run into these kinds of issues, you give me a ping. So analyse.

Them: It says to me the most invoices endpoint is returning a 404. It looks like the API doesn't support invoice listing in the current integration. Let me just share my screen. Paste in my ear. Maybe I need to do something more. And I it was working right for you, Quincy. And I was working for me as well. It was.

Me: Is it working for you today?

Them: So.

Me: Kirsty?

Them: Give me the server before getting a 4-1 era. I think it's got to do with the keys.

Me: So 404 is not anything to do with the keys. Is this what everyone's getting or is everyone getting something different?

Them: Getting a. Oh, sorry, kissy. You go. No, say I'm getting 4-1 authentication error. The moss API keys aren't being picked up correctly. A few things. To try. To regenerate the keys.

Me: Can you keep your. Screen up?

Them: Okay.

Me: I just want to check the installation. Can. You. Queen, see, can you open up the terminal? And I need to see your whole screen? And not just the. Quad. The cloud window. Sorry. Can you change your screen sharing so it's just. The whole thing? Yeah, thanks terminal. And then I've pasted command into the chat of this. Conversation.

Them: Oh, chat.

Me: Yeah.

Them: Okay.

Me: Sorry.

Them: So I copy the whole thing from open.

Me: Let's see what this has to say. So who has access to the EPA keys in moss? It's not everyone is it? Kirsty and Annelise. Or?

Them: No, I do. I may admin use it for just Edmund.

Me: Sorry, can I see your keys again? What. Am I?

Them: See, those don't look like your keys that we looked at on Friday.

Me: So someone wanna.

Them: I'm just trying to. Kill it.

Me: See. So the one that is called clawed queen sea is the one I've been using. Kirsty and Annelise. Do you know which ones you're using?

Them: Yeah, I'm using that one that says I'm using the bottom one.

Me: And curse the which one are you using?

Them: Second from the bottom.

Me: The one that ends in e7 z.

Them: Yeah, I'm looking at here in terminal.

Me: Okay. Cool. And sorry, analysts, you're using the bottom one.

Them: Yeah, the a.

Me: Okay. What is it? S7d. Queen see which one are you actually using? Cloud queen c2.

Them: H. How do I check that?

Me: That's what's in your in the screen here at the top.

Them: 70? Oh, so I think it's this one 70.

Me: And then again, Kirsty and Annelise the command that is on queen sees. Configuration. Do you guys have the similar thing? Oh, quincy go to cube at the top. Yep.

Them: Yeah. And we have a look. What am I searching for to get this at the terminal?

Me: You want to show your screen. I can help sort of guide you through it.

Them: Other open.

Me: And then queency. Sorry, can you go back into claude again and let's see. Remind me what your error was.

Them: Search. Thing.

Me: Quincy, can you ask, can you and Claude just say. Use. This. And maybe Kirsty, can you try that question as well?

Them: Is mask connected to. What is a month end. Duel?

Me: I don't know. Annelise told me it's a thing that should be done. I can't remember what it does. We can ask about in a second once we know.

Them: I want it to help me with my.

Me: Yeah.

Them: Thing.

Me: I think it does a good job. But that's one of the questions I want to ask.

Them: It's a skill there, though. I'm sure. I don't know if we, if they put onto your machine, but try their quency and see.

Me: But yeah, I mean, quincy, let's see if this is working. Sorry, did you manage to check your installation was working? Do you want something?

Them: No. How do they do that?

Me: If you want to share your screen. And. Quincy, can you open up a new chart and ask us something about moss? To say use the moss MCP connection in a new chat? And I think it's got lots of memory about the things that we did last time. And then also just where it says sonnet. For move that up to opus. Yeah. This doesn't need the month end. Just be like, use the most NCP connection to tell me to fetch some data.

Them: Okay.

Me: And then yeah, on at least if you go into the. Terminal.

Them: Yeah.

Me: And you see in the chat there's a command that says open dash a terminal.

Them: What pattern do I need to copy that, like, from open or from. The library?

Me: To the end of JSON. Fail. Ures. No. So on at least users is not installed.

Them: But if you go, if you, if you go into prod and you look at enveloper run.

Me: Sure. I think this is the one that you tried to make like a month ago. Kirsty, that index.js file.

Them: Yeah. So maybe we need to just reinstall. But look, Quincy, what quincy has is what is not this js node run?

Me: No, no. So Quincy.

Them: S?

Me: Let's, let's go back to coinciding and see if it works.

Them: Is running mcp. So. I'll stop sharing for this.

Me: V1 expenses. So I think the one that Quincy has is old. And the one that annelise has is older. So.

Them: Install. Tom, if we can go through your installation. I mean.

Me: Give that a go.

Them: Yeah. Yeah. Let's give that a go. Let's do that in the next 10 minutes.

Me: All right. So. It's getting summer, but it's, this is the old version, Quincy. Do you want to just press the stop button at the bottom? At the bottom right here? How have you guys been installing this?

Them: It's. Yeah. So. It's been a mixture of people installing it. And I landed up installing on dave and alias's machine. Yes, it is the older version, but I didn't think it would make a difference, so. But obviously it is making a difference. So let's just install your latest version and see if that's what the issue is.

Me: All right, so. Let me post this into. Tech finance. Channel. Can you all go to the tech finance channel and slack and download that zip file? So coincidence. If you open up that folder in the downloads and let's wait and see finally sync kirsty are there. Yet. It's called moss MTP server dash main.

Them: Yeah.

Me: And at least there as well.

Them: Okay. Done.

Me: No, what's the easiest way of doing this? Can you. Sorry just go back a bit so you're in your downloads folder? Yeah. And then go into the terminal. And then type. Cd space. And then you want to drag that moss MCP server main folder into your terminal. After you've typed cd space.

Them: Privileges on.

Me: You don't need admin privileges, I don't think.

Them: Do I press enter? Here?

Me: What's that? Sorry?

Them: Do I press enter here?

Me: Press enter there. Let's just pause and see how analyse and kirsty are doing with this.

Them: Yeah.

Me: Manage. Ment.

Them: Looks the same as quincy.

Me: Yeah. And then type. Just type this in here. That one. Bash installed bash space install dot sh.

Them: No such file or directory.

Me: Then what's, let's try queen suit. Yep. Annelise, do you want to. Share your screen? Means we missed the step earlier if you get that.

Them: Okay. Something that's failed.

Me: Okay. Let me just check that one. You can see. Ignored. Queens taking scroll to the bottom. That's it at the bottom.

Them: Yeah, this is the end.

Me: Okay. Give me a second. Chrissy, how are you getting on?

Them: Yeah, it's installed for me. And so, yeah, it's all good. I think it's because I've got all python and everything installed.

Me: Here. We go. What's going on here? Cool. So green, see you got to the end. Let's go to the bottom. So kirsty, did you get the same message at the bottom of queen sees the screen?

Them: No, mine installed.

Me: But that is the message you get at the end of the install. So I suspect you haven't. Do you want to. Just check?

Them: Quincy says their bash install no such file or directory. Seeing on the screen. No, that's me. Sorry. I don't know what quincy. I can't see. Quincy screen anymore. But it's definitely installed.

Me: Kirsty, you want to share your screen? I just have a look. I can see. All.

Them: Yeah.

Me: It's. A can you press? Make sure you're in the terminal. I think you have caps lock on because your cd is uppercase. It should just be lowercase cv. So press up. On.

Them: I think I did that.

Me: Yeah. So do you want to.

Them: I thought.

Me: Try that again? So cd.

Them: Space. CD and then drop the file.

Me: No, no, you got a whole lot of stuff on your on your travel just now.

Them: In.

Me: Let's press down, down, down, down, down, down, down. Yeah, let's try it now. So cd. Space. And then just copy and paste the rest of the command from the one above. So slash users slash. Oh yeah, that works too. Oh, there's a, you need a space between cd and the first slash. And you can't use the cursor. You don't have to press left until you get there. Okay now the. Back.

Them: And then paste the bash.

Me: Space install.sh. Where is kirsty, you sharing your screen just now?

Them: But I can just waiting for you. I want to take away at least the screen. S doing things in the background. Yeah, it's definitely installed. Yeah.

Me: Kirsty. Here. Yeah.

Them: I've come opened up the file. Can see the keys that are there.

Me: So that's not what it asks you to do at the top. Let's scroll up a little bit. So paste this inside your ncp server's object moss command and args. Look at the command and the args that you've got kirsty. Those are different.

Them: Okay. All right. So just to paste those in. Okay, cool. I'll paste those in.

Me: Yeah, I need to change all that.

Them: Now. Put the keys that I've got in there. Then. Paste this inside the mcp survey. I place the key values in the mask. I have an. App or when you have.

Me: The one that quincy had. Let's. See. What. Let's try that again. Because something wrong with your python installation.

Them: To do the cd again.

Me: No just the bash installed on sh.

Them: Do I have item? I just the best.

Me: Ould have.

Them: Is what it said last time as well. And then you have the error.

Me: Queen cc at the bottom there where you've got command and args. Can you copy those two lines? With command all the way to the end of python and args all the way to the end of the comma. So just those two lines command and args. Yeah you need the core as well but yep and then all the way there and then copy that.

Them: Is this?

Me: Not the m just to the. Yep. No no and he's in text edit.

Them: It? Here?

Me: You've got text edit open down in your dock. It's like kind of a page with a pen on it.

Them: Sorry. Where is that? Your symbols at the bottom.

Me: In the dock all your applications are white page with a pen on it.

Them: Say the symbols.

Me: At the bottom of your screen. Kind of in the mid.

Them: Right at the bottom. Couldn't see this. One.

Me: Dle.

Them: Okay.

Me: So then if you want to leave these these where you going? There you go so you see there's command and arcs. Needed to again select from the quote mark on command down to the comma after args. Down a bit down a bit. That's it. Press delete. And then delete one more time. And then paste. Cool I just press delete you've got extra space there.

Them: Sorry. What do I do from here?

Me: Just press the delete key one time. And then save that. And close the window.

Them: Control just command s? To save?

Me: Yeah yeah come on desk. And then. Yeah I think that's that's what it should look like. And then in clod. You want to quit claude and reopen it. And Kirsty how's yours getting on did you manage to change your.

Them: I'm connected. So it's. It was the installation. You like. I just thought we could just power through because I already got us 90 of the way then. It was saying we were up and running. But, yep, it was the installation, so that's my bed. Sorry. Busy with other things. It's been like last priority for me. So.

Me: So here we go here's queen c and a lease is screen. You still get the same error don't you Anneliese? So yeah queen see just ask a question about mods don't start on a new rule starting a new chat always start always good starting a new chat.

Them: I still have the error. And do I need to say that use the most mcp connection?

Me: What. The hell is wrong. With that lease? S?

Them: I think that's why I just, like, try to push through with one that I had written up. And then working. And then it looked great. And then it did work. And then it stopped working.

Me: Yeah it doesn't have it doesn't it doesn't have the right API the first one I sent didn't have the right API configuration either so that's why it's running.

Them: And so. Yeah. Yeah. Apologize for that, because I've actually. And this hasn't been a priority for me, so I'm sorry. It's distracting.

Me: This way.

Them: On and off.

Me: Yay I was low Kwin's up and running so Kirsty you have something similar to what he has.

Them: Yeah, I'm up and running. So what I can do is just sit with Jaden and David as well, just to get this working. Now I can see that 100 needs this install.

Me: Yeah yeah it does and if we do ever change. If we ever make updates to this that install script will just copy the new version you'd have to download it again into your downloads folder and then that and at least if you want to stay on I can help you with yours if we got five more minutes?

Them: Ment.

Me: Yeah.

Them: Stay on because I'm gonna help Jaden, Dave. So if they're gonna run into the same issues, which they probably are, then I can just figure out how to debug it with them.

Me: Yeah. Okay. And at least I have. Quincy how's that looking looking. What's it got? The date filter is ignored. From day. Into day. Cursed what will happen when you asked a query did you get this paid pagination issue. Or. What did you get?

Them: Like monthly data. Not days. Month level. Yeah.

Me: Sure try that? Kirsty what was your what was your question that you asked that you got a good answer for.

Them: I just asked to give me the last. Five expenses. And just gave me a list of them. I can ask.

Me: Yeah Quincy you want to try that can you give me the last five?

Them: More.

Me: Expenses? From moss? And then Anneliese I've sent you a command copy and paste into your terminal it's in your slack.

Them: Okay. Just pulling that up. Can I paste it in the same terminal area?

Me: Yep. Cursory.

Them: I was gonna say at the end, if you could just run me through exactly what's in this installation. So I understand better because I obviously can see that it makes a difference.

Me: Yeah sure and then Annelise can you. Try the bash installed on sh again or actually. Yeah go on try bash install dot.

Them: I still have an error.

Me: Can you run. This one python dash dash version? And your tinted dune slack?

Them: Can I not count.

Me: Let's try. Weird. Yeah but it did okay so. Can you. Press command and key in your terminal. And then run the bash install thing again? Queen see what's this response like. Once it's seen to you.

Them: Just. Just going through, actually.

Me: So is this like an expenses versus invoice nomenclature type thing or what's it?

Them: Yeah. So the expenses are differentiated in different types, like car transactions, invoices and reimbursements. So I just asked it to give me a specific, like, invoices for June, but it doesn't look like it gives it like that.

Me: But it's because it expected to call them expenses as opposed to invoices. That's why it's or what is that am I reading that right?

Them: No, I didn't get to you. Sorry.

Me: It's that because it expects you to talk about expenses as opposed to invoices and it's because it's saying I don't have a type so I don't know which of these are invoices and which of them are really.

Them: Yes. Kind of like that. Because the. The first question which I asked, it gave me. It gave me the list of expenses, but these. These were all undercut transactions. But it is. It doesn't. Like, know how to pull out different separately. Yeah. Because then most there. Yeah. So the world is different things. Our transactions and more experience separate through.

Me: Got you okay so. At least I have no idea what's going on with your python installation sorry I'm gonna have to get someone aim on this one but like. What we're running into here with the expenses and invoices so as far as I saw. There isn't like an invoices API endpoint.

Them: Lisa, you tried taking that error and just pasting it into claud. Just asking it. The. This one I'm highlighting. And say we're getting this error. And then just also with the command you hit run. It.

Me: Analysts let's not let's not let's I think this is a python error I'm gonna spend a bit more time on this I am gonna have to go in five minutes but I wouldn't dig deeper on claude getting to change on your machine.

Them: Okay. Okay.

Me: But can you copy and paste that error and send it to me in slack?

Them: When you say the air, do you want, like, the whole red thing?

Me: Yeah the whole thing yeah. Command.

Them: Okay, I just copy this all so you can see what I tried to do. I've seen it to you on slack. Whatever you says for this, please. Please just let me know as well, because I was running into issues with jades computer and everything and why I just went with the other installation.

Me: Yeah.

Them: With. And. And so because I was getting so frustrated with getting trying to get this sorted. So I think that's why we got it up and running. But then I clearly can see that that's now having that installation doesn't work long term. So I recognize that now. So let me know whatever this is, and I'll try not to help them.

Me: Will do. Once I work out what this is. Kirsty you wanted to like go through what's in the new one this make it a bit technical I literally have five minutes.

Them: In your diary. Yeah.

Me: Like Quincy and Alice if you want to drop off it's fine so the new one. I think the problem with both our old ones was that it wasn't following the API. Request so like this is the expect so you you can get all expenses and you by calling this endpoint. The type here that it gets yeah so like queen sees problem where it was tailored that it can't get the type that doesn't sound right because it should be able to tell the difference between card transactions invoices and reimbursements so Quincy while you're here if you say give me the last 10 expenses and tell me their types we could see if it's able to see the types. So yeah so Kirsty the problem with our old versions was that it wasn't asking for the right things like it wasn't sending the authentication header right it wasn't. It wasn't dealing with. Like API limits that you can only make one quest like a handful of API calls per per second so to do things like the month end report requests like all expenses for the last year. And that was that was timing out but that's that's all been fixed. In the new version and the new version is so Kirsty you should be able to see this the new version is off here in server.py. Thing is in here about how it connects to mocks and what it does. Can we expenses expenses expenses.

Them: I see. Okay. Wow. All right. I grossly underestimated what needed to be done here. I do apologize. It's been really top of my priority list. Sort of just been, like, helping out. And I think in my mind, I was like, if we can just connect. By the mcp, I didn't realize the Granola detail that we needed to specify, like these different calls. Like you've just shown in the screen. So I apologize. I thought we had. But I didn't actually understand the context of where all the issues were. So, yeah, I dropped the ball on this one a bit.

Me: Yeah. No no no so ideally if we can get everyone on this version and then things like if it's if it's saying things like I don't know the type then we can fix that.

Them: Yeah. We can fix that. I understand.

Me: We can absolutely fix that if you want to ask like I just want to see the invoices then we can because right now there's just a get expenses and then you just have to filter it by invoices if you're always asking for just the invoices or just the card transactions then we can teach it to do a better job of that but to do that I. Need everyone to have it installed and send me problems that they run into so like queen see at the top right of your clawed chat you should have the ability to share that chat with me if you want to go ahead and share that with me then I'll be able to see like what problems it has with expenses and so on and we can make this better.

Them: Okay. Okay. No, this makes a lot of sense. I don't think I fully appreciate it, actually, how you needed to make changes to the quick, you know, the queries you were sending to the apis. I see now. Why. And I was struggling with getting it installed with this python. Exactly. We've seen it, at least whatever. Like, this works. I can get working. Let's just get it on their machines now see that that is not.

Me: And now have a go at the file one that Christian was asking about as well because that's in this it's like our old AP our old connectors just didn't know how to ask for that whereas this this one does know how to ask for that.

Them: Okay, I understand. No, when you said if we do updates to this, they don't need to install it again, or we do.

Me: You do but it should be a bit easier. Yeah.

Them: Okay, so we just have to do, like, another version of this installation, install it again. Okay. I have learned a lot here today. Yeah. Great. I'll. I'll go now and try and get this installed on jade and dave and Christian's computer and just see if they're having issues. And please let me know what you figure out with analisa, because I'm probably going to run into the same issue.

Me: Yeah.

Them: On their machines.

Me: I don't know yeah make it lucky.

Them: You know, it's so interesting is because our machines are set up as developers. Like, a lot of this stuff's been done before when we've been installing python and everything, gone through those pains before without remembering. I've even been through those. So for me, it's been quick. But then with their, a lot of the stuff isn't installed, like python and all these good things. So, yeah, these are some of the blocks that I've been running into, and I think you, you've seen now. Yeah.

Me: All right.

Them: Okay. Can I ask, is a net suite connected to. Claud?

Me: Is net suite connected yes it is ask Jaren he'll tell you how to get to him.

Them: Okay. Like, if I want some information from net suit with, like, claud me the correct information.

Me: Yes it should do hang on a second. Here is. I just pinged you in the slack.

Them: Yeah, because it gave me more information, tom.

Me: I really need to go doctor's appointment but if penguins like where it is and I'll catch you guys later thanks.

Them: On, on.
