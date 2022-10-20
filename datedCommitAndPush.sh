if [ $# -eq 0 ] ; then
        echo "No args supplied -- do a ./datedCommitAndPush.sh help to see how ya do it."
        exit

fi

if [ $1 == "help" ] ; then
        echo "This thing takes 5 args -- a filename, a commit message, and a month, day, and year."
        echo "like ./datedCommitAndPush.sh <fileToCommit> <commit message> <date>"
        echo "date is like month day year e.g. Sept 21 2022"
        exit

fi

git add $1

git commit -m "$2" --date "$3 $4 14:00 $5 -0800"

git push origin main -f