{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":95,"position":95,"stack":[[{"start":{"row":120,"column":4},"end":{"row":120,"column":9},"action":"remove","lines":["ramen"],"id":6},{"start":{"row":120,"column":4},"end":{"row":120,"column":20},"action":"insert","lines":["mongo.db.ramens."]}],[{"start":{"row":120,"column":19},"end":{"row":120,"column":20},"action":"remove","lines":["."],"id":7}],[{"start":{"row":54,"column":35},"end":{"row":54,"column":42},"action":"remove","lines":["flavour"],"id":12},{"start":{"row":54,"column":35},"end":{"row":54,"column":36},"action":"insert","lines":["c"]},{"start":{"row":54,"column":36},"end":{"row":54,"column":37},"action":"insert","lines":["o"]},{"start":{"row":54,"column":37},"end":{"row":54,"column":38},"action":"insert","lines":["u"]},{"start":{"row":54,"column":38},"end":{"row":54,"column":39},"action":"insert","lines":["n"]},{"start":{"row":54,"column":39},"end":{"row":54,"column":40},"action":"insert","lines":["t"]},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["r"]},{"start":{"row":54,"column":41},"end":{"row":54,"column":42},"action":"insert","lines":["y"]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "],"id":13},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":14}],[{"start":{"row":62,"column":0},"end":{"row":70,"column":126},"action":"insert","lines":["@app.route('/search_recipes/', methods=[\"GET\", \"POST\"])","def search_recipes():","    if request.method == \"POST\":","        post_request = request.form.get('searchbar_input')","        print(post_request)","    return render_template(\"search_recipe.html\",","                            local_category=mongo.db.categories.find(), ","                            recipes=mongo.db.recipes.find({\"title\" : {\"$regex\": post_request, \"$options\": \"i\"}}),","                            recipe_count=mongo.db.recipes.find({\"title\" : {\"$regex\": post_request, \"$options\": \"i\"}}).count())"],"id":15}],[{"start":{"row":70,"column":126},"end":{"row":70,"column":130},"action":"remove","lines":["    "],"id":16},{"start":{"row":70,"column":126},"end":{"row":71,"column":0},"action":"insert","lines":["",""]},{"start":{"row":71,"column":0},"end":{"row":71,"column":28},"action":"insert","lines":["                            "]}],[{"start":{"row":62,"column":13},"end":{"row":62,"column":27},"action":"remove","lines":["search_recipes"],"id":17},{"start":{"row":62,"column":13},"end":{"row":62,"column":25},"action":"insert","lines":["search_ramen"]}],[{"start":{"row":63,"column":4},"end":{"row":63,"column":18},"action":"remove","lines":["search_recipes"],"id":18},{"start":{"row":63,"column":4},"end":{"row":63,"column":16},"action":"insert","lines":["search_ramen"]}],[{"start":{"row":65,"column":41},"end":{"row":65,"column":56},"action":"remove","lines":["searchbar_input"],"id":19},{"start":{"row":65,"column":41},"end":{"row":65,"column":42},"action":"insert","lines":["q"]},{"start":{"row":65,"column":42},"end":{"row":65,"column":43},"action":"insert","lines":["u"]},{"start":{"row":65,"column":43},"end":{"row":65,"column":44},"action":"insert","lines":["e"]},{"start":{"row":65,"column":44},"end":{"row":65,"column":45},"action":"insert","lines":["r"]},{"start":{"row":65,"column":45},"end":{"row":65,"column":46},"action":"insert","lines":["u"]}],[{"start":{"row":65,"column":45},"end":{"row":65,"column":46},"action":"remove","lines":["u"],"id":20}],[{"start":{"row":65,"column":45},"end":{"row":65,"column":46},"action":"insert","lines":["y"],"id":21}],[{"start":{"row":67,"column":34},"end":{"row":67,"column":41},"action":"remove","lines":["_recipe"],"id":22}],[{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"insert","lines":["r"],"id":23},{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"insert","lines":["a"]},{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"insert","lines":["m"]},{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"insert","lines":["e"]},{"start":{"row":67,"column":32},"end":{"row":67,"column":33},"action":"insert","lines":["n"]},{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"insert","lines":["_"]}],[{"start":{"row":70,"column":39},"end":{"row":70,"column":40},"action":"remove","lines":["t"],"id":24},{"start":{"row":70,"column":38},"end":{"row":70,"column":39},"action":"remove","lines":["n"]},{"start":{"row":70,"column":37},"end":{"row":70,"column":38},"action":"remove","lines":["u"]},{"start":{"row":70,"column":36},"end":{"row":70,"column":37},"action":"remove","lines":["o"]},{"start":{"row":70,"column":35},"end":{"row":70,"column":36},"action":"remove","lines":["c"]}],[{"start":{"row":69,"column":112},"end":{"row":70,"column":120},"action":"remove","lines":[",","                            recipe_=mongo.db.recipes.find({\"title\" : {\"$regex\": post_request, \"$options\": \"i\"}}).count()"],"id":25}],[{"start":{"row":69,"column":28},"end":{"row":69,"column":35},"action":"remove","lines":["recipes"],"id":26},{"start":{"row":69,"column":28},"end":{"row":69,"column":40},"action":"insert","lines":["ramen_search"]}],[{"start":{"row":69,"column":50},"end":{"row":69,"column":57},"action":"remove","lines":["recipes"],"id":27},{"start":{"row":69,"column":50},"end":{"row":69,"column":51},"action":"insert","lines":["r"]},{"start":{"row":69,"column":51},"end":{"row":69,"column":52},"action":"insert","lines":["a"]},{"start":{"row":69,"column":52},"end":{"row":69,"column":53},"action":"insert","lines":["m"]},{"start":{"row":69,"column":53},"end":{"row":69,"column":54},"action":"insert","lines":["e"]},{"start":{"row":69,"column":54},"end":{"row":69,"column":55},"action":"insert","lines":["n"]},{"start":{"row":69,"column":55},"end":{"row":69,"column":56},"action":"insert","lines":["s"]}],[{"start":{"row":69,"column":64},"end":{"row":69,"column":69},"action":"remove","lines":["title"],"id":28},{"start":{"row":69,"column":64},"end":{"row":69,"column":65},"action":"insert","lines":["f"]},{"start":{"row":69,"column":65},"end":{"row":69,"column":66},"action":"insert","lines":["l"]},{"start":{"row":69,"column":66},"end":{"row":69,"column":67},"action":"insert","lines":["a"]},{"start":{"row":69,"column":67},"end":{"row":69,"column":68},"action":"insert","lines":["v"]},{"start":{"row":69,"column":68},"end":{"row":69,"column":69},"action":"insert","lines":["o"]},{"start":{"row":69,"column":69},"end":{"row":69,"column":70},"action":"insert","lines":["u"]},{"start":{"row":69,"column":70},"end":{"row":69,"column":71},"action":"insert","lines":["r"]}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":30},"action":"insert","lines":["# "],"id":29}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":30},"action":"remove","lines":["# "],"id":31}],[{"start":{"row":68,"column":52},"end":{"row":68,"column":62},"action":"remove","lines":["categories"],"id":32},{"start":{"row":68,"column":52},"end":{"row":68,"column":53},"action":"insert","lines":["r"]},{"start":{"row":68,"column":53},"end":{"row":68,"column":54},"action":"insert","lines":["a"]},{"start":{"row":68,"column":54},"end":{"row":68,"column":55},"action":"insert","lines":["m"]},{"start":{"row":68,"column":55},"end":{"row":68,"column":56},"action":"insert","lines":["e"]},{"start":{"row":68,"column":56},"end":{"row":68,"column":57},"action":"insert","lines":["n"]},{"start":{"row":68,"column":57},"end":{"row":68,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":67,"column":47},"end":{"row":68,"column":67},"action":"remove","lines":["","                            local_category=mongo.db.ramens.find(), "],"id":33},{"start":{"row":67,"column":47},"end":{"row":68,"column":0},"action":"remove","lines":["",""]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]}],[{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "],"id":34},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]},{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"remove","lines":[" "]}],[{"start":{"row":67,"column":47},"end":{"row":67,"column":48},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "],"id":36},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"remove","lines":["# "],"id":37},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"remove","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"remove","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"remove","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"remove","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"remove","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"remove","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"remove","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"remove","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":54,"column":35},"end":{"row":54,"column":42},"action":"remove","lines":["country"],"id":38},{"start":{"row":54,"column":35},"end":{"row":54,"column":36},"action":"insert","lines":["f"]},{"start":{"row":54,"column":36},"end":{"row":54,"column":37},"action":"insert","lines":["l"]},{"start":{"row":54,"column":37},"end":{"row":54,"column":38},"action":"insert","lines":["a"]},{"start":{"row":54,"column":38},"end":{"row":54,"column":39},"action":"insert","lines":["v"]},{"start":{"row":54,"column":39},"end":{"row":54,"column":40},"action":"insert","lines":["o"]},{"start":{"row":54,"column":40},"end":{"row":54,"column":41},"action":"insert","lines":["u"]},{"start":{"row":54,"column":41},"end":{"row":54,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "],"id":40},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":41}],[{"start":{"row":62,"column":0},"end":{"row":73,"column":109},"action":"insert","lines":["@app.route('/search_ramen')","def search_ramen():","    orig_query = request.args['query']","    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}","    print(query)","    results=mongo.db.ramens.find({'flavour': query})","    ","    ramen = []","    for result in results:","        ramen.append(result)","    ","    return render_template('ramen_search.html', title=\"Search Results\", query=orig_query, ramen_search=ramen)"],"id":42}],[{"start":{"row":73,"column":109},"end":{"row":74,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":64,"column":24},"end":{"row":64,"column":29},"action":"remove","lines":[".args"],"id":45},{"start":{"row":64,"column":24},"end":{"row":64,"column":33},"action":"insert","lines":[".form.get"]}],[{"start":{"row":65,"column":4},"end":{"row":65,"column":6},"action":"insert","lines":["# "],"id":46}],[{"start":{"row":66,"column":4},"end":{"row":66,"column":6},"action":"insert","lines":["# "],"id":47}],[{"start":{"row":67,"column":45},"end":{"row":67,"column":50},"action":"remove","lines":["query"],"id":48},{"start":{"row":67,"column":45},"end":{"row":67,"column":86},"action":"insert","lines":[" {\"$regex\": post_request, \"$options\": \"i\""]}],[{"start":{"row":67,"column":86},"end":{"row":67,"column":87},"action":"insert","lines":["}"],"id":49}],[{"start":{"row":67,"column":57},"end":{"row":67,"column":69},"action":"remove","lines":["post_request"],"id":50},{"start":{"row":67,"column":57},"end":{"row":67,"column":67},"action":"insert","lines":["orig_query"]}],[{"start":{"row":62,"column":27},"end":{"row":62,"column":52},"action":"insert","lines":[", methods=[\"GET\", \"POST\"]"],"id":82}],[{"start":{"row":62,"column":52},"end":{"row":62,"column":53},"action":"insert","lines":[")"],"id":83}],[{"start":{"row":62,"column":52},"end":{"row":62,"column":53},"action":"remove","lines":[")"],"id":84}],[{"start":{"row":62,"column":52},"end":{"row":62,"column":53},"action":"insert","lines":[")"],"id":85}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"remove","lines":["# "],"id":86}],[{"start":{"row":62,"column":0},"end":{"row":62,"column":53},"action":"remove","lines":["@app.route('/search_ramen'), methods=[\"GET\", \"POST\"])"],"id":87},{"start":{"row":62,"column":0},"end":{"row":62,"column":53},"action":"insert","lines":["@app.route('/search_ramen/', methods=[\"GET\", \"POST\"])"]}],[{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "],"id":88}],[{"start":{"row":64,"column":4},"end":{"row":64,"column":42},"action":"remove","lines":["orig_query = request.form.get['query']"],"id":89},{"start":{"row":64,"column":4},"end":{"row":64,"column":44},"action":"insert","lines":["post_request = request.form.get('query')"]}],[{"start":{"row":67,"column":57},"end":{"row":67,"column":67},"action":"remove","lines":["orig_query"],"id":90},{"start":{"row":67,"column":57},"end":{"row":67,"column":69},"action":"insert","lines":["post_request"]}],[{"start":{"row":73,"column":78},"end":{"row":73,"column":88},"action":"remove","lines":["orig_query"],"id":91},{"start":{"row":73,"column":78},"end":{"row":73,"column":90},"action":"insert","lines":["post_request"]}],[{"start":{"row":65,"column":2},"end":{"row":65,"column":82},"action":"remove","lines":["  # query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}"],"id":92},{"start":{"row":65,"column":1},"end":{"row":65,"column":2},"action":"remove","lines":[" "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":1},"action":"remove","lines":[" "]},{"start":{"row":64,"column":44},"end":{"row":65,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":65,"column":4},"end":{"row":65,"column":6},"action":"remove","lines":["# "],"id":93}],[{"start":{"row":64,"column":4},"end":{"row":64,"column":16},"action":"remove","lines":["post_request"],"id":94},{"start":{"row":64,"column":4},"end":{"row":64,"column":16},"action":"insert","lines":["post_request"]}],[{"start":{"row":65,"column":10},"end":{"row":65,"column":15},"action":"remove","lines":["query"],"id":95},{"start":{"row":65,"column":10},"end":{"row":65,"column":22},"action":"insert","lines":["post_request"]}],[{"start":{"row":62,"column":0},"end":{"row":72,"column":111},"action":"remove","lines":["@app.route('/search_ramen/', methods=[\"GET\", \"POST\"])","def search_ramen():","    post_request = request.form.get('query')","    print(post_request)","    results=mongo.db.ramens.find({'flavour':  {\"$regex\": post_request, \"$options\": \"i\"}})","    ","    ramen = []","    for result in results:","        ramen.append(result)","    ","    return render_template('ramen_search.html', title=\"Search Results\", query=post_request, ramen_search=ramen)"],"id":96},{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"remove","lines":["# "],"id":97},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"remove","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"remove","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"remove","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"remove","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":61,"column":0},"end":{"row":69,"column":3},"action":"remove","lines":["","    ","@app.route('/search_ramen/', methods=[\"GET\", \"POST\"])","def search_ramen():","    if request.method == \"POST\":","        post_request = request.form.get('query')","        print(post_request)","    return render_template(\"ramen_search.html\", ramen_search=mongo.db.ramens.find({\"flavour\" : {\"$regex\": post_request, \"$options\": \"i\"}}))","   "],"id":98}],[{"start":{"row":61,"column":0},"end":{"row":69,"column":126},"action":"insert","lines":["@app.route('/search_recipes/', methods=[\"GET\", \"POST\"])","def search_recipes():","    if request.method == \"POST\":","        post_request = request.form.get('searchbar_input')","        print(post_request)","    return render_template(\"search_recipe.html\",","                            local_category=mongo.db.categories.find(), ","                            recipes=mongo.db.recipes.find({\"title\" : {\"$regex\": post_request, \"$options\": \"i\"}}),","                            recipe_count=mongo.db.recipes.find({\"title\" : {\"$regex\": post_request, \"$options\": \"i\"}}).count())"],"id":99}],[{"start":{"row":69,"column":126},"end":{"row":69,"column":151},"action":"remove","lines":["                         "],"id":100},{"start":{"row":69,"column":126},"end":{"row":70,"column":0},"action":"insert","lines":["",""]},{"start":{"row":70,"column":0},"end":{"row":70,"column":28},"action":"insert","lines":["                            "]}],[{"start":{"row":60,"column":111},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":101}],[{"start":{"row":62,"column":13},"end":{"row":62,"column":27},"action":"remove","lines":["search_recipes"],"id":102},{"start":{"row":62,"column":13},"end":{"row":62,"column":25},"action":"insert","lines":["search_ramen"]}],[{"start":{"row":63,"column":4},"end":{"row":63,"column":18},"action":"remove","lines":["search_recipes"],"id":103},{"start":{"row":63,"column":4},"end":{"row":63,"column":16},"action":"insert","lines":["search_ramen"]}],[{"start":{"row":65,"column":41},"end":{"row":65,"column":56},"action":"remove","lines":["searchbar_input"],"id":104},{"start":{"row":65,"column":41},"end":{"row":65,"column":42},"action":"insert","lines":["q"]},{"start":{"row":65,"column":42},"end":{"row":65,"column":43},"action":"insert","lines":["u"]},{"start":{"row":65,"column":43},"end":{"row":65,"column":44},"action":"insert","lines":["e"]},{"start":{"row":65,"column":44},"end":{"row":65,"column":45},"action":"insert","lines":["r"]},{"start":{"row":65,"column":45},"end":{"row":65,"column":46},"action":"insert","lines":["y"]}],[{"start":{"row":67,"column":28},"end":{"row":67,"column":41},"action":"remove","lines":["search_recipe"],"id":106},{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"insert","lines":["r"]},{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"insert","lines":["a"]},{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"insert","lines":["m"]},{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"insert","lines":["e"]},{"start":{"row":67,"column":32},"end":{"row":67,"column":33},"action":"insert","lines":["n"]},{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"insert","lines":["."]}],[{"start":{"row":67,"column":34},"end":{"row":67,"column":35},"action":"insert","lines":["s"],"id":107},{"start":{"row":67,"column":35},"end":{"row":67,"column":36},"action":"insert","lines":["e"]},{"start":{"row":67,"column":36},"end":{"row":67,"column":37},"action":"insert","lines":["a"]},{"start":{"row":67,"column":37},"end":{"row":67,"column":38},"action":"insert","lines":["r"]},{"start":{"row":67,"column":38},"end":{"row":67,"column":39},"action":"insert","lines":["c"]},{"start":{"row":67,"column":39},"end":{"row":67,"column":40},"action":"insert","lines":["h"]}],[{"start":{"row":68,"column":28},"end":{"row":68,"column":30},"action":"insert","lines":["# "],"id":108}],[{"start":{"row":70,"column":28},"end":{"row":70,"column":34},"action":"remove","lines":["recipe"],"id":109},{"start":{"row":70,"column":28},"end":{"row":70,"column":29},"action":"insert","lines":["r"]},{"start":{"row":70,"column":29},"end":{"row":70,"column":30},"action":"insert","lines":["a"]},{"start":{"row":70,"column":30},"end":{"row":70,"column":31},"action":"insert","lines":["m"]},{"start":{"row":70,"column":31},"end":{"row":70,"column":32},"action":"insert","lines":["e"]},{"start":{"row":70,"column":32},"end":{"row":70,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":49},"end":{"row":70,"column":56},"action":"remove","lines":["recipes"],"id":110},{"start":{"row":70,"column":49},"end":{"row":70,"column":50},"action":"insert","lines":["r"]},{"start":{"row":70,"column":50},"end":{"row":70,"column":51},"action":"insert","lines":["a"]},{"start":{"row":70,"column":51},"end":{"row":70,"column":52},"action":"insert","lines":["m"]},{"start":{"row":70,"column":52},"end":{"row":70,"column":53},"action":"insert","lines":["e"]},{"start":{"row":70,"column":53},"end":{"row":70,"column":54},"action":"insert","lines":["n"]},{"start":{"row":70,"column":54},"end":{"row":70,"column":55},"action":"insert","lines":["s"]}],[{"start":{"row":69,"column":45},"end":{"row":69,"column":52},"action":"remove","lines":["recipes"],"id":111},{"start":{"row":69,"column":45},"end":{"row":69,"column":51},"action":"insert","lines":["ramens"]}],[{"start":{"row":69,"column":28},"end":{"row":69,"column":35},"action":"remove","lines":["recipes"],"id":112},{"start":{"row":69,"column":28},"end":{"row":69,"column":29},"action":"insert","lines":["r"]},{"start":{"row":69,"column":29},"end":{"row":69,"column":30},"action":"insert","lines":["a"]},{"start":{"row":69,"column":30},"end":{"row":69,"column":31},"action":"insert","lines":["m"]},{"start":{"row":69,"column":31},"end":{"row":69,"column":32},"action":"insert","lines":["e"]},{"start":{"row":69,"column":32},"end":{"row":69,"column":33},"action":"insert","lines":["n"]},{"start":{"row":69,"column":33},"end":{"row":69,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":64,"column":4},"end":{"row":64,"column":6},"action":"insert","lines":["# "],"id":113}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":114},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":69,"column":78},"end":{"row":69,"column":79},"action":"insert","lines":["s"],"id":115},{"start":{"row":69,"column":79},"end":{"row":69,"column":80},"action":"insert","lines":["t"]},{"start":{"row":69,"column":80},"end":{"row":69,"column":81},"action":"insert","lines":["r"]},{"start":{"row":69,"column":81},"end":{"row":69,"column":82},"action":"insert","lines":["("]}],[{"start":{"row":69,"column":94},"end":{"row":69,"column":95},"action":"insert","lines":[")"],"id":116}],[{"start":{"row":70,"column":83},"end":{"row":70,"column":84},"action":"insert","lines":["s"],"id":117},{"start":{"row":70,"column":84},"end":{"row":70,"column":85},"action":"insert","lines":["t"]},{"start":{"row":70,"column":85},"end":{"row":70,"column":86},"action":"insert","lines":["r"]},{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"insert","lines":["("]}],[{"start":{"row":70,"column":99},"end":{"row":70,"column":100},"action":"insert","lines":[")"],"id":118}],[{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"remove","lines":["."],"id":119}],[{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"insert","lines":["_"],"id":120}],[{"start":{"row":69,"column":28},"end":{"row":69,"column":34},"action":"remove","lines":["ramens"],"id":121},{"start":{"row":69,"column":28},"end":{"row":69,"column":40},"action":"insert","lines":["ramen_search"]}],[{"start":{"row":68,"column":72},"end":{"row":68,"column":73},"action":"remove","lines":[" "],"id":123},{"start":{"row":68,"column":72},"end":{"row":69,"column":0},"action":"insert","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":69,"column":28},"action":"insert","lines":["                            "]},{"start":{"row":69,"column":28},"end":{"row":69,"column":29},"action":"insert","lines":["q"]},{"start":{"row":69,"column":29},"end":{"row":69,"column":30},"action":"insert","lines":["u"]},{"start":{"row":69,"column":30},"end":{"row":69,"column":31},"action":"insert","lines":["e"]},{"start":{"row":69,"column":31},"end":{"row":69,"column":32},"action":"insert","lines":["r"]},{"start":{"row":69,"column":32},"end":{"row":69,"column":33},"action":"insert","lines":["y"]}],[{"start":{"row":69,"column":33},"end":{"row":69,"column":34},"action":"insert","lines":["="],"id":124}],[{"start":{"row":69,"column":34},"end":{"row":69,"column":35},"action":"insert","lines":["p"],"id":125},{"start":{"row":69,"column":35},"end":{"row":69,"column":36},"action":"insert","lines":["o"]},{"start":{"row":69,"column":36},"end":{"row":69,"column":37},"action":"insert","lines":["s"]},{"start":{"row":69,"column":37},"end":{"row":69,"column":38},"action":"insert","lines":["t"]},{"start":{"row":69,"column":38},"end":{"row":69,"column":39},"action":"insert","lines":["_"]},{"start":{"row":69,"column":39},"end":{"row":69,"column":40},"action":"insert","lines":["r"]},{"start":{"row":69,"column":40},"end":{"row":69,"column":41},"action":"insert","lines":["e"]},{"start":{"row":69,"column":41},"end":{"row":69,"column":42},"action":"insert","lines":["q"]},{"start":{"row":69,"column":42},"end":{"row":69,"column":43},"action":"insert","lines":["u"]},{"start":{"row":69,"column":43},"end":{"row":69,"column":44},"action":"insert","lines":["e"]},{"start":{"row":69,"column":44},"end":{"row":69,"column":45},"action":"insert","lines":["s"]},{"start":{"row":69,"column":45},"end":{"row":69,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":69,"column":46},"end":{"row":69,"column":47},"action":"insert","lines":[","],"id":126}],[{"start":{"row":65,"column":19},"end":{"row":65,"column":20},"action":"insert","lines":["s"],"id":127},{"start":{"row":65,"column":20},"end":{"row":65,"column":21},"action":"insert","lines":["t"]},{"start":{"row":65,"column":21},"end":{"row":65,"column":22},"action":"insert","lines":["r"]},{"start":{"row":65,"column":22},"end":{"row":65,"column":23},"action":"insert","lines":["("]}],[{"start":{"row":65,"column":48},"end":{"row":65,"column":49},"action":"insert","lines":[")"],"id":128}],[{"start":{"row":65,"column":19},"end":{"row":65,"column":49},"action":"remove","lines":["str(request.form.get('query'))"],"id":129},{"start":{"row":65,"column":19},"end":{"row":65,"column":40},"action":"insert","lines":["request.args['query']"]}],[{"start":{"row":70,"column":87},"end":{"row":70,"column":88},"action":"remove","lines":["("],"id":130},{"start":{"row":70,"column":86},"end":{"row":70,"column":87},"action":"remove","lines":["r"]},{"start":{"row":70,"column":85},"end":{"row":70,"column":86},"action":"remove","lines":["t"]},{"start":{"row":70,"column":84},"end":{"row":70,"column":85},"action":"remove","lines":["s"]}],[{"start":{"row":70,"column":96},"end":{"row":70,"column":97},"action":"remove","lines":[")"],"id":131}],[{"start":{"row":71,"column":99},"end":{"row":71,"column":100},"action":"remove","lines":[")"],"id":132}],[{"start":{"row":71,"column":86},"end":{"row":71,"column":87},"action":"remove","lines":["("],"id":133},{"start":{"row":71,"column":85},"end":{"row":71,"column":86},"action":"remove","lines":["r"]},{"start":{"row":71,"column":84},"end":{"row":71,"column":85},"action":"remove","lines":["t"]},{"start":{"row":71,"column":83},"end":{"row":71,"column":84},"action":"remove","lines":["s"]}],[{"start":{"row":68,"column":72},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":134},{"start":{"row":69,"column":0},"end":{"row":69,"column":28},"action":"insert","lines":["                            "]}],[{"start":{"row":69,"column":28},"end":{"row":69,"column":50},"action":"insert","lines":["title=\"Search Results\""],"id":135}],[{"start":{"row":69,"column":50},"end":{"row":69,"column":51},"action":"insert","lines":[","],"id":136}],[{"start":{"row":67,"column":47},"end":{"row":68,"column":72},"action":"remove","lines":["","                            # local_category=mongo.db.categories.find(),"],"id":137}],[{"start":{"row":65,"column":19},"end":{"row":65,"column":20},"action":"insert","lines":["t"],"id":140},{"start":{"row":65,"column":20},"end":{"row":65,"column":21},"action":"insert","lines":["y"]}],[{"start":{"row":65,"column":20},"end":{"row":65,"column":21},"action":"remove","lines":["y"],"id":141},{"start":{"row":65,"column":19},"end":{"row":65,"column":20},"action":"remove","lines":["t"]}],[{"start":{"row":70,"column":64},"end":{"row":70,"column":69},"action":"remove","lines":["title"],"id":149},{"start":{"row":70,"column":64},"end":{"row":70,"column":65},"action":"insert","lines":["f"]},{"start":{"row":70,"column":65},"end":{"row":70,"column":66},"action":"insert","lines":["l"]},{"start":{"row":70,"column":66},"end":{"row":70,"column":67},"action":"insert","lines":["a"]},{"start":{"row":70,"column":67},"end":{"row":70,"column":68},"action":"insert","lines":["v"]},{"start":{"row":70,"column":68},"end":{"row":70,"column":69},"action":"insert","lines":["o"]},{"start":{"row":70,"column":69},"end":{"row":70,"column":70},"action":"insert","lines":["u"]},{"start":{"row":70,"column":70},"end":{"row":70,"column":71},"action":"insert","lines":["r"]}],[{"start":{"row":71,"column":63},"end":{"row":71,"column":68},"action":"remove","lines":["title"],"id":150},{"start":{"row":71,"column":63},"end":{"row":71,"column":70},"action":"insert","lines":["flavour"]}],[{"start":{"row":64,"column":4},"end":{"row":64,"column":6},"action":"remove","lines":["# "],"id":152}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "],"id":151},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":714.5625,"scrollleft":0,"selection":{"start":{"row":64,"column":34},"end":{"row":64,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":46,"state":"start","mode":"ace/mode/python"}},"timestamp":1578986344241,"hash":"76a5d1fe568392ab6a0d36a668aab8d9d86dfc6f"}