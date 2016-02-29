<html>
    <body>
        <table>
            <tr>
                <th>
                    Task
                </th>
                <th>
                    Due date
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
