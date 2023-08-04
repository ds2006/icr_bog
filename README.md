# Modernizing Models of Care for Psychology: Using online, self-guided, low-intensity support to make a difference. 

This project intends to collect and assess the mental health of individuals and their children, both through manual surveys and an online forum as a potential alternative to traditional family therapy methods. By using both techniques to measure the progress of individuals over time, a final treatment plan can be determined, whether that be a SSI (Single-Session Intervention) if the individuals are continuing to fare negatively, or successful completion of the program should it prove successful for the individual.s

Modules containing relevant techniques were introduced to patients, with a survey being adminstered each week to determine the progress of the patient. To simulate the community aspect of typical group therapy, a forum was created through use of Lemmy, a free and open source software with the ability to host online conversations. A sentiment analysis software known as Vader was then used to analyze the conversations between individuals based on their level of emotion. Subsequently, the survey data was processed and compared to the results gathered from the forum. Both means were used to examine the progress of the patient, as well as the potential next steps.  


# How to access the slides:
```
libreoffice --headless --convert-to pdf presentation_icr.odp
```
# How to install docker and docker-compose:

### Docker and docker compose prerequisites
```
sudo apt-get install curl
sudo apt-get install gnupg
sudo apt-get install ca-certificates
sudo apt-get install lsb-release
```

### Download the docker gpg file to Ubuntu
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Add Docker and docker compose support to the Ubuntu's packages list
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginsudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginlinux/ubuntu   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
### Install docker and docker compose on Ubuntu
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
 ```
### Verify the Docker and docker compose install on Ubuntu
```
sudo docker run hello-world
```

### After these commands have been run, reboot your computer with:

```
sudo reboot
```

### Then open up a new terminal and type:
```
groups
```
### Make sure that when you type groups, that docker shows up. 

### If docker does not show up type the following:
```
sudo adduser *username*  docker
```


# How to install Lemmy with Docker:

### Create a folder for the lemmy files. the location doesnt matter, you can put this anywhere you want
```
mkdir lemmy
cd lemmy
```

### Create the yml and hjson files that will create an instance
```
wget https://raw.githubusercontent.com/LemmyNet/lemmy-ansible/main/templates/docker-compose.yml
wget https://raw.githubusercontent.com/LemmyNet/lemmy-ansible/main/examples/config.hjson -O lemmy.hjson
wget https://raw.githubusercontent.com/LemmyNet/lemmy-ansible/main/templates/nginx_internal.conf
```

### Get into the yml file, and change any fields with {{}}
```
nano docker-compose.yml
```
### Get into the hjson field, and change any fields with {{}}  ** make sure that the fields match in passwords and domains
```
nano lemmy.hjson 
```
### Set the correct permissions for pictrs folder:
```
mkdir -p volumes/pictrs
sudo chown -R 991:991 volumes/pictrs
```


### Run these commands to bring up the lemmy container
```
docker-compose up -d
docker-compose logs -f
```


### Open the browser and type in:
```
localhost: *your port number* (1234 or 8536 are common ones)
```

# How to run the Sentiment Analysis program:

### Run the below command (in the terminal with the dollar prompt) to access all of the posts from your lemmy instance:
```
docker exec lemmy_postgres_1 /usr/local/bin/psql -U lemmy -d lemmy -c "select * from post;"
```
**if the above command does not work, you may need to change the _ to a -
```
docker exec lemmy-postgres-1 /usr/local/bin/psql -U lemmy -d lemmy -c "select * from post;"
```
### Run one of the below commands to access all of the comments for a post:
```
docker exec lemmy_postgres_1 /usr/local/bin/psql -U lemmy -d lemmy -c "select * from comment;"

docker exec lemmy-postgres-1 /usr/local/bin/psql -U lemmy -d lemmy -c "select * from comment;"
```

### Run the below command to save those comments to a csv file (with a | delimieter) 
```
docker exec lemmy-postgres-1 /usr/local/bin/psql -U lemmy -d lemmy -c "select * from comment;" > 'input_file_name_here'.csv
```
### Run the csv file through pgadmin4 to correct any formatting issues using the newTable.py code, but change the following:
```
python3 newTable.py
```
 conn = psycopg2.connect(host="host_name", dbname = "databasename", user="postgres",
                        password = "password", port=5432)

 FROM 'FILE.csv'

 dataPhase.to_csv('EXPORT_FILE.csv', index=False)



### Run, but change the following:
```
python3 sentiment_lemmy_comments.py
```

 df=pd.read_csv("INSERT CSV FILE NAME HERE (The one that is now cleaned up).csv")

 f = open('ENTER OUTPUT FILE NAME HERE.csv', 'w')

### The sentiment analysis has run on your lemmy comments, and the file can be accessed at the name of the output file name.csv 

# Downloading pgAdmin4 for Ubuntu
You can use the following tutorial: https://www.youtube.com/watch?v=tducLYZzElo

### Start by installing PostgreSQL

### Create the file repository configuration:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

### Import the repository signing key:
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
### Update the package lists:
```
sudo apt-get update
```
### Install the latest version of PostgreSQL.
### If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
```
sudo apt-get -y install postgresql
```
### Now execute the following command in Terminal. This will open the postgres prompt. 
```
sudo -i -u postgres
```	
### In the Postgres prompt, type
```
createdb my_pgdb
```
### This will create the database with the name my_pgdb

### Next, type
```
psql -d my_pgdb
```	
### To get the connection information, in the my_pgdb prompt, type
```
\conninfo
```	
### Then open a new terminal in your home directory to setup your repository. 

### Install the public key for the repository using the following command
```
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages pgadmin-org.gpg
```
### You may need to install curl first, using
```
sudo apt install curl
```
### Create the repository configuration file
```
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```
### Install pgAdmin for desktop (Web mode not required)
```
sudo apt install pgadmin4-desktop
```
> If you install it for the Web mode, be sure to configure the webserver using sudo /usr/pgadmin4/bin/setup-web.sh

### Before opening pgAdmin4, set your password. First, open the postgres terminal by entering the following commands in the terminal. 
```
sudo -i -u postgres
```
### Then:
```
psql
```
### In the postgres prompt, type the following:
```
\password postgres
```
### In the prompt, choose your new password. Hit enter, then enter it again. 

### Open pgAdmin4. Navigate to the Server bar. Then right click to register a server. 

### When registering your server, use the following terms:
```
Name: localhost
Port: 5432
Host name/address: Your IP address
Username: postgres
Password: <The password you chose earlier>
```
### You should now be able to create the databases of your choice. The database my_pgdb should already be there

	
	















