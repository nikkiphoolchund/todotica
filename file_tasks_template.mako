<html>
    <body>
        <table>
            <tr>
                <th>
                    Task
                </th>
                <th>
                    Date due
                </th>
            </tr>
            % for task in tasks:
                <tr>
                    <td>${task.name}</td>
                    <td>${task.due_date}
                </tr>
            % endfor
        </table>
    </body>
</html>
