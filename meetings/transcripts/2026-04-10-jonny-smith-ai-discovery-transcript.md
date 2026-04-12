---
title: Tom <> Jonny AI Discovery — transcript
meeting: 2026-04-10-jonny-smith-ai-discovery
created: 2026-04-10
type: transcript
---

Me: All right, Jonny. Good, man. Good. How you doing?

Them: Yeah not bad it's Friday slightly sunny.

Me: Nice. That's good. Some almost to the weekend to see if the sun stays out.

Them: Hello hopefully although I think it's raining all weekend so great.

Me: So, yeah, I wanted to reach out and find out how you're getting on with AI. And if I can help it anyway, I know there were some times you've asked in the past about zapier or any and. There's lots going on around the company. I just want to get a Vape check on where everyone's at.

Them: I use the basic sort of AI stuff in like chat GPT clone Granola those sorts of things and that's probably the stuff that I use most. At the moment I've obviously used chat GPT more heavily when I was doing some of the zappier stuff. I think.

Me: That was to, like, help you build the zapier workflows.

Them: Yeah so obviously yeah so as you because obviously I didn't know anything about how to build zapier so I was asking how to do certain things in it. It probably I'd probably say it wasn't 100 accurate you know in terms of the advice that it gave but it kind of pointed me in the direction of what to look at. Did you like a bit of googling as well to get certain things over the line but I found it quite useful in terms of like pointing you in a direction when you don't know what you're doing. I probably would say that they're not that they're not. Absolute solution you know like chat GP doesn't know everything but it can point you in the direction which I think is quite a decent but I definitely wouldn't use it as like verbatim for anything. Like.

Me: And you still use, like, Google and, I guess, tutorials around Google or, like, the classic is always like a YouTube thing about how to build your things. So you're still using those.

Them: I'll do a little bit of a hybrid because I think. Sometimes you can what you can do is like you can throw it into chat GPC like super generic and then it will point you in the direction it'll give you some advice and you can kind of take that more granula stuff from chat GPT and then probably maybe had to find a forum on online. Absolutely fine tune it but you know that's a lot easier to get you a lot further down the line I think with the AI usage which is good. I think I've had a mess around with the MCP but I think I've got a little bit of bee for that at the moment. So you know when you sort of ask it like telematics data and for analytics and that sort of stuff.

Me: Connectivity things or what kind of things you're asking.

Them: Yeah you know like. You like data quality and tripping consistencies all that sort of stuff.

Me: Yeah.

Them: I haven't noted all this down yet it's on my list of things to do that seems to keep growing. But I think it needs some more education around like certain, you know like parameters and that sort of stuff because I've had a couple of scenarios where. Customers said something. MCP then sort of contradicts it but then sort of my own experience from telematics tells me that mcp is not right if that makes sense. A little bit more educational you know like certain parameters I think things like GPS fix is a great example that it doesn't recognize as a.

Me: As a quality computer. Sorry. Go on. GPS recognize.

Them: So like it'll obviously knows that GPS fixes there but it doesn't understand gps fix as a method for determining whether the quality of that data point is any good or not. Makes sense so this vehicle's definitely done 100 mile 190 mile an hour and I'm like it's not because it's GPS fixes suit is really low. So you wouldn't you know you would exclude that data point because GPS fix isn't accurate enough to provide you with the best data possible to determine speed. You can kind of then it can argue with you and be like no it definitely did and it's like no.

Me: But you're able to see the GPS fix in that kind of response that it gives you. Are you. Or you were like, tell me the GPS fix. What was the.

Them: Yeah so I'm more like I'll probably it'll come back to me but like this vehicle did 190 mile an hour so like a custom will say to me we've done this same we did 190 mile an hour but we didn't that's impossible so you'll sort of go to query in mcp and it'll be like, yeah, it did. 190 mile an hour and you're like no it's not so then I'll say well what was the GPS fix at that point and it'd be like oh gps fix was three and I'm like well that's really low. So that's a problem for speeding.

Me: So you were going back and forward with it and, like, getting. It's not like showing you the data and you've seen the GPS fix. You had to, like, go in and ask, like, what's the GPS fix?

Them: Yeah.

Me: The customer's coming to you because the portal shows them at 190 as well.

Them: Yeah so the portal's showing like 190. So I think I've figured out the problem with tech this has been going on for the last couple of weeks so we know that there's a there's a fix at the tech guys need to release in the data to kind of get rid of all that stuff anyway.

Me: Yeah.

Them: Because they weren't they're not been doing it at the start but I think it's it's it's the sort of. I think I feel like I feel like at the moment and I'm not I can't prove this for absolute verbatim until I've done some more analysis but I feel like it probably just needs a little bit more education in terms of like giving advice on. Like data quality being you know like being good and bad just you know what parameters it needs to look for when it's when it's determining like good data quality because I think it's still accepting data as good that's maybe not quite good.

Me: And that's not just for the MTP or for the AI. That's, like, for the portal as well. No.

Them: Yeah I've already spoke to tech about it around what they need to get rid of. For this.

Me: Steve, what's the. Who'd you go?

Them: Yeah I suppose about it so that we've got a mass there's a huge thread on going at the moment where we're looking at data quality different. Sort of intervals so there's been a bit of a problem with nanos where we've been getting loads of like really high speeding alerts on the one hertz and it's basically because we're not doing any filtering on low GPS fix.

Me: Okay.

Them: We're just accepting low GPS fix data points. And then. That's led a lot of people to then say that it's a device fault. But it's not a device fault it's it's like standard.

Me: The day of processing. Error.

Them: Yeah so like. Because the way that. Telematics works is it's just not an absolute exact science it can't be because it's just it's a box that goes on GPS and it has an accelerometer to determine its speed and that sort of stuff but you're never going to get an absolute exact science out of any sort of market telematics device the best you'll ever get is when you do, you know, the actual ones in vehicles. You know the ones that you get the actual manufacturers telemetry that's in the bus and all that sort of stuff. If you've got those kind of devices then yeah you'll be able to get the odometer and the actual speed read it from the cam bus, but everything device that we use is a lot more basic than that.

Me: Right.

Them: So you're always going to get like these really odd. Bits of data sometimes you're always going to get like random high speeding because the devices like jumped from like one point to another on one hertz it's not been able to pinpoint exactly where it's landing on a map and it's then going to think it's gone. So you're always going to get that so you have to do your lot filtering out of the stuff where you know it's not correct. So things like low GPS fix. You normally wouldn't entertain a data point that comes from GPS that's like under five because you just know it's not connected to enough satellites to be to be accurate enough. So it's all that sort of stuff really. That. I think it's helpful the AI stuff's been helpful to uncover the problem but then I think it then needs educating back. As well at the same time.

Me: Yeah. Yeah. I mean. Without the mcp, how would you have. And someone comes to you with, like, it's one night. It says we're going to 190. What would. Your. What would you have done?

Them: Well I'll just go on the matrix data from the matrix portal look at the moment in time and see what the non one hertz data is telling me and then also have a look at the GPS fix and then I'll go to tech and say, right, this is what the non one hurts data is telling me what's the one hertz data telling you and then tech have looked at the one hurt status of where getting this data that's not included in that data. And I'm then say then saying well that can't be correct because it's not possible for the vehicle to travel 190 mile an hour. So, you know, same question what's the GPS fix like what. You know the points on a map and then that's how we've concluded effectively that that's the problem that we weren't doing any filter on it.

Me: God, it was quicker with the AI. To go through that process.

Them: I personally would say no but that's I would say. That I've worked in telematics longer than AI has.

Me: Yeah.

Them: No you know what I mean I kind of I kind of did this for the last seven years in terms of like issue diagnostics on telematics so probably. A bit easier for me to know what the problem is quicker than the AI if that makes sense because the AI is probably still learning how to identify how to identify all these problems. I guess it can only really analyze what it knows. Can't it? To an extent and what we tell it to an extent as well. I think as long as we keep feeding it back in the better it will get for customers. I think if we're going to give a customer. A customer AI, you know, in the portal like we've been showing out this last couple of weeks. It probably just needs. To be needed to be super sure that it's going to tell them the right answer and not create like this. It's a device problem when it's you know it's not a device problem sort of thing.

Me: Yeah, I get you. It's a data problem.

Them: Yeah I would say so.

Me: Is there a problem that we had before AI as well? Okay. What's your. Are you like a team of one? Yeah.

Them: I sort of latch on to other teams.

Me: Yeah. It's like, yeah, what's your, like, what's your day look like? Who do you speak to? What are you generally doing when it's not customers saying that they broke the sound barrier?

Them: A bit of a I mean I spent I work a lot with ben and daisy because I kind of do a little bit of a hybrid really of like they'll do the main scheduled calls and they've got connectivity problems. I'll jump in. And you know join the cause of the customers if they've got any specific problems to talk around or any, you know.

Me: And those generally quite technical, like connectivity problems or. Like.

Them: Hybrid to be honest it's kind of you've got customers that understand if connected and they just don't know why. So it's telling them what, you know, it's telling them why and what they need to do to resolve that because some of our customers just have no idea.

Me: They don't have the devices and the vans.

Them: Yeah it can be that they've they can they've just got loads we've sent them device and they're just not fitted them.

Me: Or. Right. Yeah.

Them: Or they have fitted in but they've not allocated the right registration so it's not showing us connected they've not given us their API credentials.

Me: Okay.

Them: They've not updated the, you know, their actual telematics provider, those sorts of things. I've also obviously been having to deal with customers at the moment querying where they'll go on their geotab account, for example. And it'll say that the vehicle's not speeding, they'll go on the flock portal and it'll say, oh, it is speeding. So we had to do a little bit of. Investigation on these differences between CSP platforms, our platform, because obviously the calculations different I think sometimes that csps use versus what we use.

Me: Yeah. That's another, like, algorithm problem for steve. For not to point.

Them: Yeah at the moment got a geotab one with matrix. Where the geotab data that we're seeing from terminal and straight from the geotub portal is different. So what we're getting from matrix. That's the latest investigation of data at the minute. And then yes, that from that it'll be follow the customers follow up with brokers. All that sort of stuff.

Me: S to our follow-ups to just, like, check it in and see what their connectivity is.

Them: Yeah so obviously the zapier stuff has all this automation that creates tickets and those sorts of things when connectivity drops but then obviously if customers don't respond to matrix then it gets escalated back towards them. We have to escalate to the broker.

Me: Like.

Them: Or we have to follow up with the client if they've contacted us basically just managing it through that.

Me: Sure.

Them: Process and then ultimately getting them through the cancellation point if they don't play along. And then triggering that process as well.

Me: And then how, when you're saying, like, someone has 75 connectivity or less than that connectivity, and it could be api keys, it could be that they're not fit. They're devices, not giving you the vrns. Like, how do you know. Which of those problems is the problem? I just gotta lose that.

Them: The general process is normal if it drops below 75% connected a ticket will go to matrix and the matrix have a like a contract oscillator contact the customer.

Me: Okay.

Them: We'll just say that customers drop below 75% of matrix or call to diagnose. One of the things I would like to be working on at some point this year is that he's absolutely relatively easy to diagnose what the problem is already like from the data that we get. We've already got some data in the in looker that tells us like the reason why it's not showing is connected. In like a bit of a ballpark. So your normal reasons will be things like. The vehicles it's on cover but we're not getting any data for that regard. No, it's an API or no it's matrix because the system already tells us that. And then we'll know if that vehicle's not on the API. Or not because we'll know if we're getting data from the API will know if there's a device that's been sent out to the customer. And it's not been installed because we'll we can see the device but we're not getting any data. We'll know if there's no device allocated to it because we won't be able to conceive whether there's a reg allocated device or not. See quite a lot of this stuff and really where I'd like to get to is that the portal can tell the customer those problems. It can either do it in. That. You know, the AI tool with demoing or it can show it in the portal. But I think I think the next step for me would be get to that point where a customer can ask an AI agent or the portable tell them. Why my vehicle is showing is not connected and it'll just. It'll just tell them. In a bit in a relatively granular detail of. You know device not showing an API.

Me: And that only shows up in liquor.

Them: Or. Yeah because I got cursed to build a calculation in Looker based on. They you know like data coming in. From matrix.

Me: Just happened priority. I mean, that doesn't sound like a great AI use case. Like, if you, if you've got an answer, just show the answer beside the vehicle kind of thing. Like, it doesn't have to be. Made up. It's quite, like, pointedly factual.

Them: I don't know what they don't know what it's there's a bit of there was a ticket log for it I think it was like last July but it's not at the moment but I don't know what the strategy is at the moment whether we're going to put more stuff into the portal. All the way or the way that we have this. AI agent that customers can ask general questions to and it gives them answers. And it obviously knows what knows what those answers are based on what the data's showing.

Me: I mean, I'm not gonna make any promises as to how to get it done. Hope to get on to my management's roadmaps. But, like, if you start talking about AI, it might muddy the waters, whereas if you're just like, here's the formula that kirsty did in liquor. Can you guys do that in the platform? Steve might do it one morning and then it's done. And then the work I had to put up little red circle with the number on it or the error message on it kind of thing. But keep it simple. I mean, again, make no promises on how to get a smell with my dirt, make some changes. Who does all this stuff when you're on holiday?

Them: Tactically play relatively well so all the follow up and all that sort of stuff are the triggers kind of by itself.

Me: Yeah.

Them: Manual follow-ups that I have to do I end up. Sort of I set the follow up dates for days when I'm not for days when I'm actually in so I'll kind of schedule everything a little bit around that in advance. And then Emily's team will pick up the inbound so when you know emails that come in from customers and brokers and that sort of stuff, they'll pick those up.

Me: When you're in holiday, otherwise you pick it up. Got you. And they've got some docks that tell them, like, how to diagnose what the reason is for the connectivity and all that kind of stuff.

Them: Yeah they've got some bits usually the inbound stuff is a little bit simpler and we're doing some training in the next few weeks so that they can actually do that stuff full time. So things like updating regions and those sorts of things. I've had an app built by matrix that kind of link this Flock branded but links to their system. So you can just update a red yourself because we'd have to send it to matrix previously on the ticket. But now we've got this little web app where you can just do it yourself. Which is quite useful.

Me: Very. Cool.

Them: So I think that's good that's going out to brokers or gone out to brokers sorry on the last. Newsletter from Liam. To use and then started to roll it out to customers and using it internally which is pretty cool.

Me: All right. Nice. Cool. All right. Thanks for the overview. Anything you wanted to ask me or complain about? Or.

Them: I don't think so I think I do need to spend a bit more time. Trying to find solutions like AI solutions for to tackle my bigger, you know, like day to day jobs that I have to spend take a bit more time. I think the barrier that I've been hitting so far is that. Places like HubSpot the data is not good enough. To sort of. Allow it to just run on its own continuously if that makes sense. So for example to trigger like all of these different zapiers do you find errors sometimes where the deal owner isn't actually the right person to contact but that's the only place I can pull the contact from. That sort of stuff. This is probably not AI that's the problem.

Me: Is the data.

Them: It's the data that it's accessing.

Me: How do you know that that's not the right owner when you look at hotspot?

Them: Get various feedback the broker will respond and be like oh it's this person that needs to contact or ben will tell me no that's not the right contact is this person they might be at the same broker company but they might not be the right person specifically for that client.

Me: Okay.

Them: There's a bit of housekeeping I think to do on like DL owners and that sort of stuff and contacts.

Me: Yeah. Because I've heard some people complain that, like, names of companies, names of clients, fleets, whatever names of brokers, names of fleets are different between, like, our platform and HubSpot, but it's also just. Like owners are wrong. And they, that kind of stuff.

Them: Yeah so I found I found out how to get rid get past the. Whole you know like broker company all those names being different I managed to that all that all works in my automations but it's the actual owners of the, you know, the actual contact is the bit that it tends to fail on the most.

Me: How'd you get past the name differences?

Them: So I used. Because you've got so you've got you've got deal ID. In the looker database. So with hubspot you can't with hubspot it's actually terrible when you're using zapier to try and search a name it doesn't actually just doesn't work it prefers to work on the actual record IDs or contact IDs really have to use that sort of stuff. So I found a really slightly long winded but workable way that pulls all the different like record IDs and you know broken name IDs and all that sort of stuff.

Me: Go.

Them: And cross searches between looker and hubspot to pull it all back again without using any any names and that and those sorts of things which works.

Me: You've got a big CSV of. Deal IDs. With names.

Them: Yes I did I did a I've done a looker integration so it's my whole zappy thing starts off looker so I've got like a looker database that will go and look in there and it will find and that will trigger a lots of different because you can do a lot more calculation in that so you can be like right this policy has hit 14 days and they've not filled out the telematics form so then it's the deal ID for that will search the deal id.

Me: Yeah.

Them: In hubspot to then pull back the primary contact id so it then knows who to send, you know, create the ticket with or send the email to and that sort of stuff. Well the problem is with that contact is wrong.

Me: Yeah.

Them: Then that's when it starts falling down but I can find the deal IDs I can find the company IDs I can find everything else with a hundred percent success. I just can't get the contact right sometimes.

Me: And you don't have the contact details on Looker. This is.

Them: You do but again they're like you have these different bits where like. You might do a deal with someone who's a sale who's in this in the sales part of a brokerage but you contact them for BAU after that might change so you could do HRIB you could write the policy with Jack Dalton but then you need to actually contact. Instead.

Me: Right. And we just don't have a good system for tracking that or for someone changing it or keeping up to date.

Them: It's manual updates people don't update the contact for the deal after they've done the deal so you'll see like you'll see the primary contact but then you'll see loads of emails after that to somebody different in the deal.

Me: The thing.

Them: Yeah they're not updating the contact after that.

Me: Oh, but you've got, like, a trace of, like, how the person that we've been contacting has changed. Like, you can see a bunch of emails. It used to go to jacket and there goes to James.

Them: Yes, you can see that in like email threads in the activity of the tick of the deal but you put your actual contact that's allocated to the deal is still Jack who you did the deal with original.

Me: I don't assume it's no one's, like, specific job to update that email.

Them: Not not really I think.

Me: Because it can change at any point in the process. So it might be like when.
