Python program that uses polynomial regression to fit a curve to a dataset using this method we can import a data set of the form:
| x | f(x) |
|---|------|
| $$x_1$$ | $f(x_1)$|
| $$x_2$$ | $f(x_2)$|
| $$x_3$$ | $f(x_3)$|
| ... | ...|
| $$x_n$$ | $$f(x_n)$$|


Which should be saved in an external file and will later be parsed onto the main file.
The program will take two arguments:


| Arguments | Description |
|---|---|
| -f | Mandatory, precedes the path for the dataset. |
| -n | Mandatory, where n is the degree of the desired polynomial for fitting. |
| -x | Optional, Label for the x axis, should be parsed using " " and along with the y axis label. |
| -y | Optional, Label for the y axis, should be parsed using " " and along with the y axis label. |

Finally, the program is to be used as follows on the console:
```console
foo@bar:~$ python3 main.py -f filePath -n N
```
Or, in case that the graph of the function is needed:
```console
foo@bar:~$ python3 main.py -f filePath -n N -x "xlabel" -y "ylabel"
```

Please let me know if there are any questions.


