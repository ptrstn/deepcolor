import React, { RefObject } from "react";


interface HeaderLinksProps {
}
interface HeaderLinksState {
    links: Map<string, string>;
    name: string;
}

export class HeaderLinks extends React.Component<HeaderLinksProps, HeaderLinksState> {
    private readonly imageRef: RefObject<HTMLDivElement> = React.createRef();

    constructor(props: HeaderLinksState) {
        super(props);
        this.state = {links: new Map([["About", "#"], ["GitHub", "https://github.com/INF-HS-KL-BEGGEL/DL-SS20-T1-image-col"], ["Contact", "#"]]), name: "Imaginator"};
    }

    render() {
        return (<header>
                    <ul>
                        <li className="left"><a href="#"><h1 className="logo">{this.state.name}</h1></a></li>
                        {Array.from(this.state.links)
                        .map((element, i) => {
                            return (
                            <li key={i}><a href={element[1]}>{element[0]}</a></li>
                            )
                        })}
                    </ul>
                </header>);
    }
}