import React, {useState, useEffect} from 'react';
import './App.css';
import {Configuration, Game, LobbyApi} from "./api-client";

function App() {
    // const openapiConfig = new Configuration(
    //     {
    //         basePath: "http://localhost:8080"
    //     }
    // );
    const openapi = new LobbyApi();

    const [games, setGames] = useState<Game[]>([]);

    useEffect(() => {
        openapi.gamesGet().then((res) => {
            setGames(res.data);
        }).catch((err) => {
            console.log(err);
        });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Games</h1>
                Create new game <button>Create</button>

                <table>
                    <thead>
                    <tr>
                        <th>Id</th>
                        <th>Host Name</th>
                        <th>Guest Name</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {games.map((game) => (
                        <tr key={game.id}>
                            <td>{game.id}</td>
                            <td>{game.host?.name}</td>
                            <td>{game.guest?.name}</td>
                            <td>{game.status}</td>
                            <td>
                                <button>Edit</button>
                                <button>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </header>
        </div>
    );
}

export default App;
