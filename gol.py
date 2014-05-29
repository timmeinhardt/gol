#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)
app.debug = True

class Cell():
    future = 0
    def __init__(self,x,y,alive):
        self.alive = alive
        self.x = x
        self.y = y

    def destiny_executer(self,World):
    	destiny_count = 0
    	for x in range(self.x-1,self.x+2):
    		for y in range(self.y-1,self.y+2):
    			    destiny_count += World[x][y].alive


    	destiny_count = destiny_count - self.alive

    	if destiny_count == 2 and self.alive == 1:   
    	    self.future = 1
    	elif destiny_count == 3:
    		self.future = 1
    	else:
    	    self.future = 0

@app.route('/<multi>', methods=['GET', 'POST'])
def view(multi):
    global population_multi 
    population_multi = int(multi)
    for x in range(population_multi):
        World[x]= {y:Cell(x,y,0) for y in range(population_multi)}
    return render_template("gol.html", population_multi=population_multi)

@app.route('/start', methods=['POST'])
def start():
    x = int(request.form["x"])
    y = int(request.form["y"])
    if World[x][y].alive == 0:
        World[x][y].alive = 1
    else:
        World[x][y].alive = 0
    return "none"

@app.route('/live', methods=['GET', 'POST'])
def execute():
    for x in range(1,population_multi-1):
            for y in range(1,population_multi-1):
                World[x][y].destiny_executer(World)
    for x in range(1,population_multi-1):
        for y in range(1,population_multi-1):
            World[x][y].alive = World[x][y].future            
    world_alive = dict((x,dict((y,World[x][y].alive) for y in range(population_multi))) for x in range(population_multi))
    return jsonify(world_alive)

if __name__ == '__main__':
    World = {}
    population_multi = 6
    app.run(host='127.0.0.1')

###circulating dict
# look at  https://github.com/wilsaj/flask-admin

    
