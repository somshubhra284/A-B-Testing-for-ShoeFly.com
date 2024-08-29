import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))
views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(views)
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
#print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
#print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
#print(clicks_pivot)

clicks_pivot['percent_clicked']=clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
#print(clicks_pivot)

clicks_count_AB=ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(clicks_count_AB)

clicks_count_AB_percentage = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().pivot(
  columns='experimental_group',
  index='is_click',
  values='user_id'
).reset_index()
#print(clicks_count_AB_percentage)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(a_clicks)
a_clicks_percent = a_clicks.groupby(['is_click','day']).count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
a_clicks_percent['percent_clicked']=a_clicks_percent[True]/(a_clicks_percent[True]+a_clicks_percent[False])
print(a_clicks_percent)

b_clicks_percent = b_clicks.groupby(['is_click','day']).count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
b_clicks_percent['percent_clicked']=b_clicks_percent[True]/(b_clicks_percent[True]+b_clicks_percent[False])
print(b_clicks_percent)