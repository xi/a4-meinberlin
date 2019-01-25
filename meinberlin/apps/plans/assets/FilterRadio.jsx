/* global django */
const React = require('react')

class FilterRadio extends React.Component {
  constructor (props) {
    super(props)

    this.state = {
      selectedChoice: this.props.chosen
    }
  }

  handleOnChange (event) {
    let choiceId = parseInt(event.target.value)
    this.props.onSelect(choiceId)
    this.setState({
      selectedChoice: choiceId
    })
  }

  isChecked (choice) {
    return (this.state.selectedChoice === choice)
  }

  render () {
    return (
      <div className="radio-group" role="group">
        <label className="" key={this.props.filterId + 'all'} htmlFor={'id_choice-' + this.props.filterId + '-all'}>
          <input
            className=""
            type="radio"
            name="question"
            id={'id_choice-' + this.props.filterId + '-all'}
            value="-1"
            checked={this.isChecked(-1)}
            onChange={this.handleOnChange.bind(this)}
          />
          <span className="">{django.gettext('all')}</span>
        </label>
        {this.props.choiceNames.map((choice, i) => {
          return (
            <label className="" key={this.props.filterId + i} htmlFor={'id_choice-' + this.props.filterId + '-' + i}>
              <input
                className=""
                type="radio"
                name="question"
                id={'id_choice-' + this.props.filterId + '-' + i}
                value={i}
                checked={this.isChecked(i)}
                onChange={this.handleOnChange.bind(this)}
              />
              <span className="">{ choice }</span>
            </label>
          )
        })}
      </div>
    )
  }
}

module.exports = FilterRadio
