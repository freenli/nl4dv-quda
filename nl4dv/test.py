import nl4dv
from vega import VegaLite
import os
dependency_parser_config = {'name': 'corenlp','model': os.path.join("../jars","stanford-english-corenlp-2018-10-05-models.jar"),'parser': os.path.join("../jars","stanford-parser.jar")}
para = nl4dv.NL4DV(data_url="nl4dv/movies-w-year.csv", dependency_parser_config=dependency_parser_config)
para.render_vis('What is the longest Running Time of the Action movies?')

# para.render_vis('Show the relationship between budget and rating for Action and Adventure movies that grossed over 100M.')
# para.render_vis('Show the relationship between budget and IMDB Rating of different Genre movies.')

# para.render_vis('Retrieve the highest IMDB Rating.')


#What is the IMDB Rating of Fargo?   1                 highlight
#What is the average value of the Worldwide Gross?  3  highlight
#How many action movies are there in this table?
#What is the largest value of the Production Budget? 4
#Sort the IMDB Rating of adventure movies. 5
#What Genres are there in this table? 6
#What is the distribution of Genre? 7
#Are there any outliers of budget? 8
#Are there any clusters of rating? 9
#What is the correlation of budget and gross? 10
#What is the correlation of budget and gross for Drama? 10
#What is the correlation of budget and gross for different Genre? 10
