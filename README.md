# Worklist Tool
The Worklist Tool is a tool for creating lists of Wikimedia pages which users can then assign themselves to for claiming and tracking work during editing events and programs.

The tool was first developed with Wikimedia during Google Summer of Code 2018.

## Usage
The Worklist Tool is hosted on Toolforge at https://tools.wmflabs.org/worklist-tool/.

Currently, the easiest way to create a Worklist is to first create a PetScan (https://petscan.wmflabs.org/) query. PetScan allows you to easily create complex lists of Wikimedia pages, such as all pages from multiple categories, or that contain particular templates, or link to specific other pages. These lists can then be imported directly into the Worklist tool.

To create a new worklist:

* Login via OAuth
* Click the Create Worklist button
* Fill out the Name and Description fields (you can leave Tags blank)
    * Description - this should be an overview of the purpose of this worklist. What kinds of articles does it include? Will it be worked on by a particular group of editors, or at a particular event?
    * Tags - These are descriptive terms for this worklist, to aid in searching.
* Enter either a PetScan Query ID or individual articles to get your list started.
* Click Submit

You can now navigate to 'See Worklists' > 'See My Worklists' in the top bar to see a list of your created worklists.

Opening a worklist will show a list of articles contained in that worklist, and allows users to claim each page. More articles can be added with the 'Add articles' button.

## Future
The vision for this tool is that it will be able to integrate with other tools, such as Citation Hunt (https://meta.wikimedia.org/wiki/Citation_Hunt). This would allow program and event organisers to create worklists of articles, assign users to them, and then import the worklist to other tools to support participants' work.

## Setup
TODO.
