## 33. Generate db table schema with GitHub Copilot Chat
[plan mode]:
Plan a very simple table schema to store shortened links

[plan mode]:
We don't want any optional fields, we need a createdAt, updatedAt, clerk user id, short code, and url to store. All dates must store the timezone data. We do not need any click tracking and deletes will be permanent i.e. NO soft deletes.

[agent mode]:
Start Implementation

[ask mode]:
is serial the best type to save an id as in the latest version of postgres?

[ask mode]:
what about generated always as identity?

[ask mode]:
how to push this schema to our postgres db hosted on neon?

[terminal]:
npx drizzle-kit push

## 34. Generate seed data with GitHub Copilot Chat and insert into db with MCP

[agent mode]:
list all of the projects in my neon account

[ask mode]:
generate 10 example links for user id [your_user_id], use the #file:schema.ts for the correct structure

[agent mode]:
insert the example data above into the [project_name_with_id] neon database
## 35. Fix redirect issue + update agent instructions 

[agent mode]:
when I sign in with clerk from the homepage it doesn't automatically redirect me to the /dashboard page. I need to refresh the browser for the redirect to work.

[agent mode]:
update the #file:AGENTS.md file to mention that it's important NEVER to use middleware.ts as this is now deprecated in later version of next js (and specifically the version of next js in this project), and instead use proxy.ts.

[agent mode (re-run previous prompt)]:
when I sign in with clerk from the homepage it doesn't automatically redirect me to the /dashboard page. I need to refresh the browser for the redirect to work.


## 36. Build out dashboard page + official way to create GitHub Copilot instructions



## 37. Convert old docs files to new GitHub Copilot instructions files

## 38 Implement create link functionality

## 39. Implement edit link and delete link functionality

## 40. Implement redirect functionality
