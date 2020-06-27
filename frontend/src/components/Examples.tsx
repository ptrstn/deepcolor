import React from "react";


interface ExampleProps {
}
interface ExampleState {
}

export class Examples extends React.Component<ExampleProps, ExampleState> {


    render() {
        return (<section id="two" className="main style2">
        <div className="container">
            <div className="row gtr-150">
                <div className="col-6 col-12-medium">
                    <header className="major">
                        <h2>Examples</h2>
                    </header>
                    <div className="row gtr-150 imgs">
						<div className="col-4 col-12-medium">
							<span className="image fit"><img src="examples/DSC_4851.jpg" alt="" /></span>
						</div>
						<div className="col-4 col-12-medium">
							<span className="image fit"><img src="examples/DSC_4912.jpg" alt="" /></span>
						</div>
						<div className="col-4 col-12-medium">
							<span className="image fit"><img src="examples/DSC_5214.jpg" alt="" /></span>
						</div>
					</div>
                </div>
            </div>
        </div>
    </section>);
    }
}