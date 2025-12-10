if [ $# -eq 1 ]; then
  mkdir day"$1"
  cd day"$1" || exit
  touch input.txt
  touch testinput.txt
  cp ../template_problem1.py ./problem1.py
  cd ..
fi
if [ $# -eq 2 ]; then
  for (( i = $1; i <= $2; i++ )); do
    mkdir day"$i"
    cd day"$i" || exit
    touch input.txt
    touch testinput.txt
    cp ../template_problem1.py ./problem1.py
    cd ..
  done
fi
if [ $# -ne 2 ] && [ $# -ne 3 ]; then
  echo "Usage: $0 <day> [<tillDay>]"
  exit 1
fi