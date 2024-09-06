# GitHub-Action-test

Detta är liftarens guide till att fatta vad 17 man håller på med

1.skapar först en html page med version information och datum
2. skapar en DOCKERFIL för projektet skriv bara in "Dockerfile"
3. Skapa en Autmate builds genom GitHub Actions med workflows som ska trigga en build varje 5 minut 
    3.1 mkdir -p .github/workflows (mkdir = skapr directory, -p= parents katalog du kan alltså skapa .github och workflow på en gång)
    3.2 annars kan du skriva så här touch .github/workflows/deploy.yml

4. Öppna nu deploy.yml här kommer workflow köra för varje push till main branch samt ska den köra varje 5 minut genom cros job!
    -----------------OBS Kolla i yml filen och kom till hit igen för att förstå lite mer-----------------------------------------
        4.1 grep "^FROM" Dockerfile letar upp raden som börjar med FROM i din Dockerfile.
        awk -F":" '{print $2}' extraherar versionsnumret från den raden. Det förväntar sig att versionsnumret kommer efter ett kolon (":").
        export VERSION=$VERSION sparar detta versionsnummer i en miljövariabel som heter VERSION.
        echo "VERSION=$VERSION" >> $GITHUB_ENV sparar versionsnumret i en GitHub-miljövariabel så att det kan användas i senare steg.

5. Skapa ett enkelt python script för att läsa in html filen samt updatera den detta. OBS! Här ska egentligen vertionen läsas in från Dockerfilen i repo Detta ska göras i gitHub ACtions-workflow. Läste något om att man kan använda grep eller något vertyg för att få ut versionnummret  men antar vi testar med "pyhton"

6. Skapa API-Token för att autmatisk kunna updatera Confluence-sidan så vi får tillstånd att skriva till sidan obs! kanske måste testa detta innan något annat. Token ska sen användas i GitHub actions-workflow för att skicka uppdatering till Confluence. Vet ej om vi gör detta via python men de ska Andripa Confluence API? via HTTP typ post- eller put- request? 
    6.1 Tips från Gorge Polare 
        1. go till repositry settings
        2. navigate to secrets and variables -> Actions secrets
        3. skapa en ny secret gh_Token med gitHub API token
        4. i workflow lägg till typ detta i yaml
                            - name: Use GitHub Token
                        env:
                            GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}
                        run: |
                            echo "Using GitHub token for authentication"
-------------------------------------------------------------------------------

7. LETS GO!!! nu kör vi
    7.1 docker build -t adam-work-dir:1.0.0 . ( i terminal för att bygg docker-bild)
    7.2 Kör docker- container på min port höö typ 8080 tror ja: docker run -d -p 8080:8080 adam-work-dir:1.0.0 
    7.3 kolla scriptet lokalt om den är samma som index.html python3 my-python.py

    borde fixat typ någon klocka istället för datum xD för att se om den updateras atomatisk men men kollar sen


8. Pusha koden till GitHub och låt workflowen köras
 8.1 git init gör repo reto i fall att
 8.2 git add . 
 8.3 git commit -m "stuff workflow docker pyhton code everyting togher"
 




