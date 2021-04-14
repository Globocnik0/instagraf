%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);">Congratulations, your file has been uploaded and a graph was made from it. Click on it to download.</h1>

            %filename = graph['filename'].split('.', 1)[0]
            %path_to_image = '/graphs_made/' + str(username) + '/' + filename + '.png'
            <a class="credit" href={{path_to_image}} download={{filename}}>
                <img src={{path_to_image}} alt="Graph"/>   
            </a>
            %end
