%rebase("base.tpl")

        <h1 style="color:rgb(59, 182, 110);"> Here are all your graphs! You can download them by clicking on it.</h1>

            %for graph in graphs:
            %filename = graph['filename'].split('.', 1)[0]
            %path_to_image = '/graphs_made/' + str(username) + '/' + filename + '.png'
            <a class="credit" href={{path_to_image}} download={{filename}}>
                <img src={{path_to_image}} alt="Graph"/>   
            </a>
            %end
