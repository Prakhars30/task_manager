# 🖥️ CLI Task Manager

> This projet was made to learn how CLI tools work, somewhat how it works, mostly how to make something like that using python I learned a lot more trying to add things I definately did not need and at one point just stopped thinking about it as a project and more of as a proper product.

I will be making this project in python and on MacOS so the experience will be highly dependent on that. 

And the whole idea is from Roadmap.sh, https://roadmap.sh/projects/task-tracker,
I just picked this up randomly

---

## 📌 Stuff to note...well it is closer to dev logs instead.

### 🚀 The Beginning

The very first one I made was a very simple one using `sys.argv` and it worked fine but there was one problem that was a pain in the a** that everytime I wanted to call it I had to write

```bash
python3 -the/whole/fu**ing/path/to/the/file- then the command
```

every single time which was OK till it was a fun little project but Absolutely not acceptable for something I planned to actually use.

So I did what everyone is doing now a days.

~~I v*be-coded it~~ I 'asked' AI for solution.

And it gave me a solution which was a `.toml` file (Learned something named TOML exist and it's full form is Tom's Obvious, something language. I forgot and I am not going back to search, you do it) then was the whole thingy about making the directory a package by using an empty `__init__.py` file , I still have no god damn clue how that works, But it works so I am keepin it for now.

---

### 💾 Storage Problems

Now comes the issue with storage.

It is not really an issue when I am using it, but according to AI (ChatGPT) it does become an issue when someone else uses it by downloading it through github, or cloning it...

It's not excatly a very good product I making it with the mentality that this will be just as good.

GPT layed it straight:

As long as I am using it using good'ol json file is no issue, the task manager data is not big or complicated enough to involve something like SQL.

But the problem how and where this file is stored because that means there are places which can not be written, only read.

That is a problem that I will not have since I can literaly hard code the location but someone else who uses this will probably not want that headache.

---

### 📦 Enter `platformdirs`

So GPT introduced me to a library called `platformdirs`.

I have this newfound love for python while building this, it's like:

> **Do You have a PROBLEM?**
>
> Here is the library that solves all of it!

Anyways, `platformdirs`, again no clue how that makes any difference but I will take it and use it.

Once again focus is not to learn the f*ck ton of libraries but getting a feel of how all these products are made and problems I never thought about that can occur.

---

This is it for Now.

I don't if i will come back to this project one maybe to practice some more useful libraries like `argparse` and the `.toml` file and the project as directory stuff.
.
.
.
.
.
Yes I used GPT to make the this README file more visually pleasing.
