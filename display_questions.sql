SELECT `questions`.`QuestionID`,
    `questions`.`QuestionText`,
    `questions`.`AnswerType`,
    `questions`.`AnswerText`,
    `questions`.`Confidence`,
    `questions`.`TopicID`
FROM `alca_db`.`questions`;
