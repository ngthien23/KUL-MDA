# KUL-MDA
 
This repositotry contains the codes for the Modern Data Analytics exam project in 2022-23

## Installation
Download and extract original data sets to base folder, extract to 'weather', 'noise events', 'noise level', 'noise percentiled'.
Some preprocessed datasets are in 'ThienNguyen/out'.


## Locations of interest
The noise locations are marked on [Google Maps](https://www.google.com/maps/@50.8747926,4.6982166,15.56z/data=!4m3!11m2!2sqrSmW6-ORGuCUEXc9dQUMQ!3e3). These locations are business venues of different types (bar, club, restaurant, hair dresser, etc.)

The availability of noise event data in 2022 is shown in the table below:

![WhatsApp Image 2023-04-30 at 2 22 12 AM](https://user-images.githubusercontent.com/85434354/235545131-95654846-42f4-403f-b819-fdf8410cd9c0.jpeg)

The lon and lat coordinates of these locations are:
```
locations = {
    'Naamsestraat 35  Maxim': (50.877264309031936, 4.700555462690086), #club
    'Naamsestraat 62 Taste': (50.87590763475016, 4.700203945323124), #bar
    'Calvariekapel KU Leuven': (50.87458499798096, 4.700163240066998), #chapel
    'Parkstraat 2 La Filosovia': (50.87414577683852, 4.700033858853713), #restaurant
 #   'bis - Vrijthof': (50.874710, 4.704792),  # not sure why this location is
    'Naamsestraat 57 Xior': (50.87662594018794, 4.70070237796116), # studenthousing
    'Naamsestraat 81': (50.87397388816172, 4.700117807627097), #building
    'His & Hears': (50.875361066623924, 4.700103994673989) #hair salon
} 
```

## More Data
The `Additional_Date` folder contains several CSV files related to the events in general or in Leuven:
- FIFA 2022 dates for each game (group stage: 22 Nov - 3 Dec) are retrieved from [here](https://www.adda247.com/school/fifa-world-cup-2022-schedule/#:~:text=2022%20Qatar%2D%20Chart-,FIFA%20World%20Cup%202022%20Schedule%20Date,globe%20in%20its%2022nd%20edition).
- KU leuven semester dates are retrived from [here](https://www.kuleuven.be/english/about-kuleuven/calendars/2021-2022/ku-leuven-leuven-main-campus).
- Concert dates in a specific hall in the center of Leuven are retrieved from [here](https://www.hetdepot.be/overzicht-concerten-corona).

## Resources
### deployed (draft)
http://mydashapp-env.eba-egg3ihi2.eu-north-1.elasticbeanstalk.com/

### explaning the model
https://towardsdatascience.com/a-novel-approach-to-feature-importance-shapley-additive-explanations-d18af30fc21b

### dynamic plots / visualization inspirations
https://towardsdatascience.com/animated-bar-plot-in-python-for-time-series-data-8809dbdf9bc
https://medium.com/@vermavinay982/dynamic-graph-plotting-matplotlib-63c94d8fa99f
https://app.flourish.studio/templates#template-time-map

### external data - building in Leuven
https://download.vlaanderen.be/Producten/Detail?id=1&title=GRBgis
https://www.mdpi.com/2071-1050/14/10/5769 

### AWS resources
https://aws.amazon.com/education/awseducate/

## Reports
The slides are accessible at [Google Drive](https://docs.google.com/presentation/d/124BeehQEYAofHWoPmbxH-LTE-0IysYX_X7drtxZiIWg/edit).
The 2-page report can be accessible at [Overleaf](https://www.overleaf.com/2187527679nrtqhjsdmhdp).
