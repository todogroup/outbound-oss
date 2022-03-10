# Appendix
## Managing work vs personal personas
In the world of open source, folks may have an online identity that pre-dates
their employment with our current organization. Simultaneously, the organization
may want contributions done on their behalf to happen with corporate emails.

To manage this, we can use a feature of git which allows different
configurations based on our directory structures.

Our `~/.gitconfig` file might look like this:

```
[user]
	name = Simba Lion
	email = simba@personal-email.example.org

[includeIf "gitdir:~/my-company/"]
    path = ~/my-company/.gitconfig
```

This sets our default persona (which, in this case, is for a personal
account). If we have repositories in the `~/my-company` directory, we'll load an
additional git config file which is located at `~/my-company/.gitconfig`. That
file might look like:

```
[user]
	email = simba@very-corporate-email.example.com
```

Now when our user commits changes, it will use their personal email by default,
or their corporate email for any repositories within the `~/my-company`
folder. Note that the name attribute is inherited from the base configuration,
so we don't need to double specify it.
