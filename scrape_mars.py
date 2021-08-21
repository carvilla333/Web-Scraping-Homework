def scrape():
    news_title = "NASA's Curiosity Mars Rover Explores a Changing Landscape"
    news_p = "A new video rings in the rover’s ninth year on Mars, letting viewers tour Curiosity’s location on a Martian mountain."
    img_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg"
    get_table = '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Mars - Earth Comparison</th>\n      <th>Mars</th>\n      <th>Earth</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Diameter:</td>\n      <td>6,779 km</td>\n      <td>12,742 km</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg</td>\n      <td>5.97 × 10^24 kg</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Moons:</td>\n      <td>2</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Distance from Sun:</td>\n      <td>227,943,824 km</td>\n      <td>149,598,262 km</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Length of Year:</td>\n      <td>687 Earth days</td>\n      <td>365.24 days</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Temperature:</td>\n      <td>-87 to -5 °C</td>\n      <td>-88 to 58°C</td>\n    </tr>\n  </tbody>\n</table>'
    image_url_list = [{'Image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
  'Picture_title': 'Cerberus Hemisphere Enhanced'},
 {'Image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
  'Picture_title': 'Schiaparelli Hemisphere Enhanced'},
 {'Image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
  'Picture_title': 'Syrtis Major Hemisphere Enhanced'},
 {'Image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
  'Picture_title': 'Valles Marineris Hemisphere Enhanced'}]

    mars_dict = {
    "news title":news_title,
    "news paragraph":news_p,
    "featured image":img_url,
    "table":get_table,
    "hemisphere images urls":image_url_list
}
    return mars_dict
