In order to run the website, download a copy of the code. Run the command
python app/view.py to run the flask server. I have also included a screen shot of the website in the root directory


Website Description:

The webpage has 3 major components to it. On the left, it has a collapsable list view of all the directories and files.
On the right, it has two components, the information table, which is a scrollable table of information about revisions of a file,
and the code, which is an iFrame that contains the actual code from subversion.

You can navigate through the directories/files on the left by clicking on the '+' to open a directory and see the files in it, or
on the '-' to collapse the tab folder that is opened. When a user clicks on a file, information about its previous revisions
it populated on the Information table and its Code is pushed onto the code iFrame.

When a user unclicks a file, both the information table and Code iFrame content is cleared.

When a user clicks on another file, the same process is repeated to generate the page.