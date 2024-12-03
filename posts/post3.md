## Intro
I've collided with the term "RPA" every now and then and thought "I need to dig into that more, but isn't that just software development? Why is it called something else?" Well, it IS something different.

Previously, I've written off anything Microsoft Office because I'm a real developer, dammit!

I've recently had the opportunity to jump into Microsoft's answer to the RPA push in industry, Power Automate. After delivering several products for about a dozen stakeholders, I think I've gotten a very good feel for what Power Automate is useful for. I share here to encourage others (devs, non-devs, and people in between) to take a closer look.

Power Automate is a no-code tool that needs a significant amount of coding knowledge to do complex things and just a computer savvy, generally curious person to do simple things (I'll explain complex vs simple).

## Some Things You Can Do with Power Automate
In no particular order:

- Automatically add a Microsoft Form submission to a SharePoint List, create a Planner task, and send an email with some key elements of the Forms submission
- Send an email and update a SharePoint List when a task is completed in Planner
- Log task completion times to a SharePoint list based on Planner task create to complete times
- Create a SharePoint folder whenever a new item is added to a SharePoint list and add the link to the SP folder in that list item
- Login to a website, enter custom filters and fields, run a report, extract it, save the report to SharePoint, and send an Teams message with a link to the report in SharePoint
- There's a ton more you could do with Power Automate including even interacting with http requests and SQL database queries and commands. I mainly focus on the aspects within the Office 365 cloud because that makes the most sense to me. If I'm getting into SQL and http endpoints, I'd rather handle that with Python and a proper SDLC.

<p style="text-align:center;font-size:20px"><strong>.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.</strong></p>
## Who Can Use Power Automate?
Repeating a line from the intro, a computer savvy and generally curious person can do simple and useful things, while complex workflows generally require a significant dev background.

Why do you need a dev background if it's no-code? For many, many workflows, you'll need for/while loops, parsing JSON payloads, conditionals/Boolean logic, variables, data types, testing skills, and strong debugging skills. These concepts start popping up a lot more in more complex workflows.

So what's a simple workflow vs a complex one? All the examples above are complex enough that you would struggle a lot without a strong development background. However, if you took one piece out of each one, that piece would be in the realm of "simple" (or at least accessible for biz users). Good news is that most "simple" workflows have ready made templates that are there by default in Power Automate. You just click, connect your account, and fill in a few details.

<p style="text-align:center;font-size:20px"><strong>.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.</strong></p>
## Insights and Observations from Working with Power Automate
I've been very impressed with it's capabilities, ease of use, and relatively painless learning curve. I was able to deliver a solution that stakeholders were excited about within a week of touching it for the first time.

### Some takeaways
- I'm impressed and will continue to use in the future
- It's not a silver bullet
- It's a valuable tool in the dev toolbox for internal org processes and products that begin and end in the Office 365 cloud
- Even if you're not doing anything in the MS cloud, you should check out Microsoft's current offerings (Power Automate, PowerBI, SharePoint, etc.) due to their ubiquity

<p style="text-align:center;font-size:20px"><strong>.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.</strong></p>
## What it's for (and some pros)
- Automating business user processes
    - Things that people are preforming (mostly) manually
    - Data and deliverables that live mainly in MS Office 365 cloud (Outlook, SharePoint, OneDrive, etc.)
- Getting applications in Office 365 cloud to talk to each other
- Automating web processes done by a user
    - Example: Someone goes to a website and uploads, downloads, or records data. Power Automate can do this for you.
- Pros
    - No infrastructure. What does that mean? Super simply, it means you don't need a server, database, or any of the overhead (labor or tech) associated with that.
    - Offers a "record actions" function that will record the clicks made by a user to make workflow creation easier. It's similar to the Excel function to record actions for macro creation.
    - Auth with the MS cloud is painless
    - It's from Microsoft, so if an org doesn't already have Power Automate available, the path there is significantly more straightforward than basically any other software (licenses and cybersecurity)
    - Matured state, albeit not categorically so (see cons)
    - Accessible to biz users with no coding experience, at least for simple workflows
    - Fast to get going for deliverables that align with "what it's for"

<p style="text-align:center;font-size:20px"><strong>.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.</strong></p>
## What it's NOT for (and some cons)
- Writing software
- Reusable code
- Complex logic
- Highly customized products (analysis, visualizations, etc.)
- Computationally intensive workloads
- Cons
    - Variables are present in Power Automate, but using them is tedious for several reasons
    - Comments...no intuitive way to include (that I can find). "Notes" are ok.
    - There are quirks if you make simple changes in your workflow. These are definitely the worst part of the learning curve with Power Automate, but hopefully they will disappear with time as Power Automate continues to mature.
    - Tech debt incurred. This is an automation solution, but there is some tech debt incurred since it's not possible to apply software dev best practices with testing, version control, reusable code, etc., etc. For me, this goes back to "it's a tool in the toolbox", use strategically. 

<p style="text-align:center;font-size:20px"><strong>.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp.</strong></p>

_Disclaimer: Wrap this whole post in parathesis with the caption, In my opinion!_