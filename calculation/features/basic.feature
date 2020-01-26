@web
Feature: Simple math quiz
	As a user,
	You want to practice basic math skills.
	So you will be adding and subtracting numbers.

	Background:
		Given you set game url
		And game is ready

	Scenario Outline: Let's check your skills
		# Given you may pick up numbers range
		# |default|10|30|40|50|60|70|80|90|100|
		When you give "<answer_type>" answer
		Then "<image_type>" image is shown

	Examples: You skills may be good or bad :-)
		| answer_type | image_type |
		| correct     | good       |
		| incorrect   | bad        |
