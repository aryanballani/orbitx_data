# OrbitX Datathon

# Final report -> https://docs.google.com/presentation/d/1KpbAZs2s7k8oDb2idVA6AP_PBec87hy7webkR5mURoM/edit#slide=id.g34872d161ee_3_110


# Plan:
## A. Region of Interest

- Canada
    - British Columbia
    - Alberta
    - North Western Territories

---

## B. Data

- Datasets
    - https://www.earthdata.nasa.gov/topics/human-dimensions/natural-hazards/data-access-tools#toc-natural-hazards-datasets

---

## C. **Step 1: Drill down to target provinces and months**

1. **Visit the NASA Earth Data Portal**
    - [NASA Natural Hazards Datasets](https://www.earthdata.nasa.gov/topics/human-dimensions/natural-hazards/data-access-tools#toc-natural-hazards-datasets)
    - Familiarize yourself with the data descriptions, sample previews, variables measured (e.g., aerosol optical depth for fires, surface temperature, etc.).
2. **Check Data Format & APIs**
    - Identify how to download or query the data: Earthdata Search, OPeNDAP, netCDF files, GeoTIFF, shapefiles, etc.
    - Make sure you know how to programmatically work with these formats in Python.
3. **Look for Additional Data Sources**
    - Government open data portals or local agencies often provide hazard-specific or region-specific data.
    - Example: For wildfires, you can combine NASA data with local fire department or US Forest Service data.

---

## D. Step 2: Identify purpose/possible reasons of a Wildfire

1. **Download or Access**
    - Acquire at least one NASA dataset relevant to your hazard and region.
    - If needed, retrieve extra supporting data (demographic data, socio-economic data, historical weather data).
2. **Data Storage & Versioning**
    - Decide on a structure: store raw data in a separate folder; keep track of file versions or use a Git repository.
3. **Data Cleaning**
    - Inspect for missing values, inconsistencies, or anomalies.
    - Convert all data to consistent units (e.g., same time zone, coordinate reference systems, etc.).
    - Document your data cleaning steps to be transparent.
- Sources for wildfires
    - https://www2.gov.bc.ca/gov/content/safety/wildfire-status/wildfire-response/what-causes-wildfire
    - https://www.canada.ca/en/public-health/services/publications/healthy-living/wildfires-canada-toolkit-public-health-authorities.html
    - https://www.nature.com/articles/s41467-024-51154-7
    - https://www.sierraclub.ca/canada-wildfire-causes/

---

## E. Step 3: Propose a solution to questions

1. **Basic Statistics & Visualizations**
    - Load your cleaned data into Python (e.g., using `pandas` or `xarray` for netCDF).
    - Generate descriptive statistics (mean, median, std) to understand distributions.
    - Create initial plots (histograms, line plots over time, maps).
2. **Mapping & Geospatial Analysis**
    - Use libraries such as `geopandas`, `rasterio`, or `folium` to visualize data on maps.
    - Overlay hazard data (e.g., wildfire perimeters, earthquake epicenters) on a regional map.
    - If you have time-series satellite data, look for trends or patterns (e.g., how a wildfire changes over days).
3. **Correlations & Patterns**
    - Check if hazard frequency correlates with certain weather phenomena or times of year.
    - Identify any pattern or cyclical trend (seasonal, monthly, yearly).
- Questions
    - **Which areas in BC are most at risk of wildfires but have limited emergency infrastructure or community resources?**
    - **Can we identify patterns in fire ignition points that could help with early detection or prevention efforts?**
    - **Are there recurring regions that need more resource allocation for wildfire response based on past trends?**

---

## F. Predictive analysis (OPTIONAL)

1. **Link Findings to Your KPIs**
    - Are hazards increasing or decreasing over time?
    - Are some regions more vulnerable than others?
2. **Propose Data-Backed Solutions**
    - Early warning systems: Could your analysis help refine early warning thresholds?
    - Resource Allocation: Which communities need the most resources based on hazard frequency or severity?
    - Policy Recommendations: For instance, *if wildfire risk is extremely high in Region X in July*, suggest more firefighting resources or public awareness campaigns then.
3. **Innovative or Predictive Approaches** *(Optional)*
    - If time allows, prototype a simple **machine learning** or **forecasting** model (e.g., using `scikit-learn`) to predict hazard probability.

---

## G. Sources and citations

1. Canadian Wildland Fire Information System. (n.d.). *CWFIS Data Mart*. Natural Resources Canada. Retrieved April 4, 2025, from https://cwfis.cfs.nrcan.gc.ca/datamart
2. Ford, M., & Burke, M. (2020). Vehicle emissions and wildfire risks: Impacts and solutions. *Environmental Science & Technology, 54*(16), 10424–10431.
3. Google Research. (n.d.). *Open Buildings Dataset*. Retrieved April 4, 2025, from https://sites.research.google/open-buildings/
4. Humanitarian Data Exchange (HDX). (n.d.). *Data for humanitarian crises and response*. United Nations OCHA. Retrieved April 4, 2025, from https://data.humdata.org/
5. Johnson, S., & Lee, A. (2019). The role of human-induced climate change in wildfire frequency. *Nature Climate Change, 9*(6), 449–456.
6. Sentinel Hub. (n.d.). *EO Browser*. Sinergise. Retrieved April 4, 2025, from https://apps.sentinel-hub.com/eo-browser/
7. Smith, J., & Li, X. (2021). Industrialization and wildfire risks: The interplay of emissions and land use. *Environmental Research Letters, 16*(7), 074012.
8. Thompson, P., et al. (2020). Climate change, industrial activity, and the escalating threat of wildfires. *Nature Sustainability, 3*(12), 905–913.
9. Williams, A., et al. (2021). Air quality, wildfires, and human health: The role of emissions from vehicles. *Journal of Environmental Protection, 12*(8), 723–731.
10. WorldPop. (n.d.). *WorldPop Datasets*. University of Southampton. Retrieved April 4, 2025, from https://www.worldpop.org/
11. Zhao, Y., & Green, R. (2019). The impact of industrial pollution on wildfire frequency. *Global Environmental Change, 58*, 101960.
12. *OGC API*. OGC API technical doc /Doc technique de l’OGC API - MSC Open Data / Données ouvertes du SMC. (n.d.). https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_en/

---

## H. Resources

- Overview
    - https://www.earthdata.nasa.gov/topics/human-dimensions/natural-hazards
- Tutorial for NASA tools
    - https://www.earthdata.nasa.gov/topics/human-dimensions/natural-hazards/learn
- Datathon main notion page
    - [https://ancient-iodine-0a0.notion.site/OrbitX-Datathon-2025-Information-Package-1cbbf35ba55c80c9aab7cd0e375856e8](https://www.notion.so/1cbbf35ba55c80c9aab7cd0e375856e8?pvs=21)
- GeoJson File Creator
    - https://geojson.io/#map=5.92/50.754/-125.305
- **Colab Notebook:** https://colab.research.google.com/drive/1rQTCi2BUqj3jRknBh6hHRnFJcOz0ZAvD?authuser=0#scrollTo=A_uxplS09WTP
- **Slides:** https://docs.google.com/presentation/d/1KpbAZs2s7k8oDb2idVA6AP_PBec87hy7webkR5mURoM/edit?usp=sharing

---

## I. Extras

1. **Stay Agile**
    - A datathon is short, so keep iterating quickly. Don’t get stuck on a single idea if it’s not panning out.
2. **Divide & Conquer**
    - Assign roles: e.g., *Data Wrangler*, *Analyst*, *Visualizer*, *Presenter*.
    - Frequent check-ins so everyone stays aligned.
3. **Document Everything**
    - Keep notes on what you tried, what worked, and what didn’t. This helps in Q&A and final reporting.
4. **Practice Your Pitch**
    - Rehearse the 5-minute presentation to ensure you stay within time.
    - Anticipate questions the judges might ask, such as “Why did you choose this region?” or “How accurate are your findings?”
    
    **1. Choose a Natural Hazard Type**
    
    - Decide which hazard(s) you want to focus on (e.g., wildfires, earthquakes, floods, etc.). You can also combine them, but often a single hazard is easier to handle.
        
        CANADIAN WILDFIRES 
        
        NASA BLOG : https://www.earthdata.nasa.gov/news/worldview-image-archive/canadian-wildfires
        
    - Brainstorm **why** you want to focus on that hazard (frequency, impact, existing knowledge, personal/team interest).
        - **Frequent & Severe**: Wildfires in BC are intense and recurring, especially during dry summer seasons.
        - **Climate-Driven**: Rising temperatures and drier conditions create a **vicious cycle**—more fires lead to more emissions, which worsen climate change and increase fire risk.
        - **Global & Local Impact**: Wildfires release massive amounts of carbon, affect air quality, damage ecosystems, and disrupt communities and local economies.
        - **Data Availability**: Rich data from NASA (e.g., MODIS, VIIRS) and local agencies provides a solid foundation for in-depth analysis.
        - **Team Motivation**: As students based in BC, we’ve seen these impacts firsthand and are passionate about creating meaningful, local solutions.
        - **Disaster Relief Relevance**: Analyzing wildfire trends can support **preparedness, mitigation, and emergency response**, aligning directly with the datathon’s goals.
    
    ### **2. Formulate Your Core Question(s)**
    
    ### Potential Questions
    
    ### 🔥 **Wildfire Trends & Behavior**
    
    - **How has the frequency and intensity of wildfires in BC changed over the last 10–20 years?**
    - **Are wildfires in BC starting earlier or lasting longer each year (i.e., has the wildfire season changed)?**
    - **What are the hotspots (geographical clusters) for wildfires in BC over the past decade?**
    
    ---
    
    ### 🌡️ **Climate & Environmental Correlation**
    
    - **Is there a correlation between surface temperature anomalies and wildfire frequency in BC?**
    - **How do drought indices or vegetation dryness correlate with wildfire ignition and spread?**
    - **How do seasonal weather patterns (e.g., temperature, precipitation) relate to wildfire severity?**
        
        ---
        
    
    ### 🌍 **Emissions & Air Quality**
    
    - **What is the estimated carbon emission from BC wildfires per year? How has this changed over time?**
    - **How far does wildfire smoke from BC typically travel, and which regions are affected by poor air quality?**
    
    ---
    
    ### 🧭 **Preparedness & Response**
    
    - **Which areas in BC are most at risk of wildfires but have limited emergency infrastructure or community resources?**
    - **Can we identify patterns in fire ignition points that could help with early detection or prevention efforts?**
    - **Are there recurring regions that need more resource allocation for wildfire response based on past trends?**
    
    ---
    
    ### 🔄 **Impact Analysis & Recovery**
    
    - **What is the impact of repeated wildfires on the same regions/ecosystems?**
    - **How quickly do affected areas recover (vegetation-wise or emission-wise) after a fire?**
    - **What are the socio-economic impacts (e.g., proximity to communities, population density, agricultural areas)?**
    
    ---
    
    ### 🧠 Bonus / Advanced (if time permits)
    
    - **Can we predict potential wildfire risk zones in BC for the upcoming season using historical and climate data?**
    - **What machine learning model best classifies high-risk wildfire zones based on environmental variables?**
    - Make sure your question(s) have a clear, measurable outcome.
    
    ### **Core Questions – Funnel Approach**
    
    We use a **funnel approach**—starting broad and progressively narrowing down to specific, actionable insights:
    
    - **Descriptive (What’s happening?)**
        1. **Which provinces** experience the most wildfires?
            
            *→ Identify top three provinces by wildfire frequency (using DRILL #1) [done]*
            
        2. **When do wildfires peak?**
            
            *→ Find the top four months with highest wildfire occurrences [done]*
            
    - **Diagnostic (Why is it happening?) (DRILL #2)**
        - Are seasonal and geographical patterns linked to temperature, precipitation, or land type?
        - Is there an increasing trend over the years, suggesting climate-driven intensification?
    - **Predictive (What could happen next?) (OPTIONAL)**
        - Can historical patterns and remote sensing data help anticipate fire-prone periods or regions?
    - **Prescriptive (What can we do about it?)**
        - How can early detection, resource allocation, or public warnings be improved using the data?
    
    ---
    
    ### **Normative vs. Pragmatic Framing**
    
    - **Normative**: *What should be done to reduce wildfire risks and their social/environmental impacts?*
        
        → Our goal is to use data to **recommend actions** for better policy, infrastructure resilience, and emergency planning.
        
    - **Pragmatic**: *Given current constraints, what are the best actionable steps?*
        
        → We aim to deliver **data-driven tools or insights** (e.g., monthly risk dashboards, hotspot maps) that help agencies act quickly and effectively, even with limited resources.
        
    
    ### **3. Define Key Performance Indicators (KPIs)**
    
    - Align them with the challenge: “help communities prepare for, respond to, or recover from these hazards.”
    - These KPIs keep your analysis focused and meaningful.
    
    KPIs from Canada Dataset  - DRILL #1
    
    1. What are the top three provinces for wildfires?
    
    1. What are top four months? 

---

## J. Visualizations

1. Top four months with most wildfires:
    
    
    month      Counts
    July         1045323
    August        989767
    September     373426
    June          359846
    

Top three provinces with most wildfires:
PRNAME                         Counts
Northwest Territories    859909
British Columbia            677954
Alberta                            608408

![wildfire_analysis.png](attachment:5f5851d5-6cbf-48ce-b490-a29119012ac7:wildfire_analysis.png)

1. 
    
    ![image.png](attachment:3830602c-1fe1-4260-9cdb-366b4091a33e:image.png)
    
    **Interpretation**
    
    1. **Temperature Cycles**
        - Each province shows a clear **seasonal cycle**: temperatures peak mid-year (summer) and drop to their lowest in winter.
        - British Columbia (BC) generally remains **warmest**, Alberta (AB) is in the **middle**, and the Northwest Territories (NT) is **coolest** year-round.
    2. **Precipitation Spikes**
        - Precipitation is **highly variable** over time, with sporadic spikes (especially in BC).
        - Overall, summer often shows **drier** periods interspersed with occasional heavy rainfall events.
    
    **Causal Relationship with Wildfires**
    
    - **Warm Summers + Dry Spells**: Higher temperatures in mid-year dry out fuels, while inconsistent precipitation leads to prolonged dry periods—both prime conditions for wildfire ignition and spread.
    - **Regional Differences**: BC’s relatively milder winters and warmer springs can **extend** the fire season; AB and NT, though cooler, still experience summer heat and occasional dryness sufficient to support significant wildfires.
2. Seasonal Temperature patterns
    
    ![image.png](attachment:dc129ac4-4391-4f0a-b204-62bddfbdce78:image.png)
    
    ### Interpretation & Causal Relationship
    
    - **Temperature:**
        
        The boxplot shows a clear seasonal cycle: low temperatures in winter and high temperatures in summer. Higher summer temperatures dry out vegetation, creating favorable conditions for wildfires.
        
    - **Precipitation:**
        
        The precipitation boxplot reveals low median rainfall during summer with occasional heavy outliers. Dry spells combined with intermittent rainfall mean that fuels remain dry for long periods, increasing fire risk.
        
    
    **Causal Link:**
    
    Higher summer temperatures and low/irregular precipitation reduce moisture in vegetation, which directly increases the likelihood of wildfire ignition and spread. This seasonal pattern is a key driver behind wildfire activity in these provinces.


---


### ***Drill#1 [DONE]***

- Climate Data → https://climate-change.canada.ca/climate-data/#/monthly-climate-summaries
    - https://climate.weather.gc.ca/prods_servs/cdn_climate_summary_e.html
    - https://eccc-msc.github.io/open-data/msc-geomet/ogc_api_en/
    - https://climate.weather.gc.ca/climate_normals/index_e.html
    - https://api.weather.gc.ca/openapi#/climate-monthly/getClimate-monthlyQueryables
    - https://cwfis.cfs.nrcan.gc.ca/report/graphs#gr1
- Feature description for FIRMS  → https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html
- https://firms.modaps.eosdis.nasa.gov/download/Readme.txt

## Comparison: MODIS vs. VIIRS

| **Aspect** | **MODIS (Terra/Aqua)** | **VIIRS (SNPP/NOAA-20)** |
| --- | --- | --- |
| **Temporal Coverage** | Available from ~2000 to present | Available from ~2012 to present |
| **Spatial Resolution** | ~1 km | ~375 m (finer detail) |
| **Data Frequency** | Twice daily (Terra and Aqua provide complementary overpasses) | More frequent overpasses due to higher revisit rate |
| **Historical Depth** | Ideal for long-term historical studies (over 20 years) | Best for recent analyses with improved spatial resolution |
| **Usage Consideration** | Suitable when long-term trends and historical comparisons are needed | Preferable if recent, high-resolution spatial details are critical |

As our focus is for recent years and you need finer spatial resolution to pinpoint small fire events, **VIIRS** might be considered. However, its shorter historical record makes it less ideal for deep temporal analysis.

NASA. (n.d.). *Fire Information for Resource Management System (FIRMS)*. NASA Earthdata. Retrieved from https://firms.modaps.eosdis.nasa.gov/

- [ ]  load 5 year data
- [ ]  EXPLORE ⇒ understand attributes needed to answer top 3 prov and top 3 months
    - [ ]  info, describe, understand
    - columns to drop
        
        satellite
        
    - columns we filtered
        
        nominal, high confidence (as we need only confident fires)
        
        sum frp
        
    
- [ ]  TRANSFORM/CLEANING ⇒ See if there isn’t any duplication of wildfires + NaN values?
    - [ ]  Remove any duplicate wildfires if any reported
    - [ ]  See if there are NaN values
    - [ ]  Any anomalies or outliers
    - [ ]  standardize esp the geo coordinates
    
- [ ]  LOAD ⇒ Load the exact three prov by spatial join with canada data [
    - [ ]  check what kind of spatial join is effective for joining

### **Drill#2 *[DONE]***

Natural hazards

for each wildfire: what are the temp trends, precip trends  ⇒ need a dataset which has climate x wildfires

**Can we find conditions that usually precede major fires — a week or two ahead?**

- Look at **7- to 14-day trends** in:
    - precipitation deficits
    - temperature anomalies
- See if there’s a **threshold combo** (e.g., <5 mm rain & >30°C for 3+ days) that usually leads to fires in a region.

✅ **Outcome:** Inform community risk dashboards or early warning systems.

### **Drill #3 *[DONE]***

industrial activities > carbon emission >  
