<p align="center"><img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=%23FFFFFF&size=25&center=true&vCenter=true&width=1000&height=100&lines=Workshop+001"></a>
</p>

#### What's this project about

Welcome to the workshop_data_engineer project! This is my first python's project, The main objective is to showcase a practical implementation of Extract, Transform, Load (ETL) processes using Python and SQLAlchemy. The project revolves around a dataset containing candidate information from a Technology company. Through various operations, we extract insights, transform data, and load it into a database for then be consumed by power bi.

#### Potential Usages

> Even when this project is not develop in a real enviroment, performing it helps to improve skills, here are following 

1. **Data Analysis and Visualization:** The project includes various data analysis and visualization tasks. You can leverage this structure to analyze hiring trends, identify popular technologies, and evaluate seniority distributions. The generated visualizations provide an intuitive way to communicate your findings.

2. **Recruitment Insights:** By examining the trends in candidate hiring, you can gain valuable insights into recruitment practices. The comparison of hiring patterns across different years and countries helps in understanding recruitment strategies' effectiveness.

3. **Decision-Making Support:** The visualized data and analytical insights can aid decision-making processes. For instance, understanding which technologies are most sought after by the company or identifying potential gaps in recruitment efforts can guide resource allocation.

4. **Database Integration Practice:** The project demonstrates database integration through SQLAlchemy. This provides a hands-on experience for those looking to enhance their database skills and understand how data flows between Python and a database system.

5. **Customization for Specific Data:** While the current project utilizes a specific dataset, the provided code can serve as a foundation for similar data-related tasks. By modifying the transformations, queries, and visualizations, you can adapt the project to analyze different datasets.

#### Folders' Structures

```
workshop_data_engineer/
├── 0_src
│   ├── main.py
│   ├── db.py
│   ├── transformation.py
├── 1_csv/                      
│   ├── hires_seniority.csv     
│   ├── hires_technology.csv    
│   ├── hires_year_and_country.csv  
│   └── hires_year.csv          
├── 2_viz/                      
│   ├── Hires_by_Seniority.png  
│   ├── Hires_by_Technology.png 
│   ├── Hires_by_year_countries.png 
│   ├── Hires_by_Year.png       
│   └── Viz.pdf                 
├── .gitignore                              
├── README.md                  
├── requirements.txt            
└──           
```

### How does it work?

To explore the potential applications of this project, follow these steps:

1. First you must go to [0_src] and create a file called [db_config.json] and store there the credentials for the database where you want to store the data 
    > If you want to get a better understanding of how this works, review the code in [0_src] to understand the structure and functionality.

2. The dashboard was perfomed using the data stored in the folder [1_csv]
3. Once you have everything set up you can run [main.py]


For any questions or assistance, feel free to reach out to Lapiceroazul at lapiceroazul@proton.me.

