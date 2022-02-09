#!/bin/bash

# Generate html files from jhtml files
echo "Generating HTML pages for Desktop -----------------------------------------"
cd calendar.d
python3 html_try-m.py > ../html_pages.d/mcalendar.html
echo "--->  month calendar generated"

echo "Generating HTML pages for Desktop -----------------------------------------"
python3 html_try-w.py > ../html_pages.d/wcalendar.html
echo "--->  week calendar generated"

cd ..
echo "Done! ------------------------------------------------------------------------  Done!"
