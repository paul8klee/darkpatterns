from website import db


# models for database structure (each one represents a questionnaire)
class DemographicData(db.Model):
    __tablename__ = 'demographic_data'
    id = db.Column(db.Integer, primary_key=True)
    prolificID = db.Column(db.String(24), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    websiteList = db.Column(db.String(1000), nullable=False)
    # create relationships to the other models to link them to the demographicData
    consentRequest = db.relationship('ModalData', backref='participant_bref', lazy=True)
    questionnaire1 = db.relationship('ControlAndDeliberationData', backref='participant_bref', lazy=True)
    questionnaire2 = db.relationship('PrivacyConcernsData', backref='participant_bref', lazy=True)

    def __repr__(self):
        return f"demographicData('{self.id}', '{self.prolificID}', '{self.gender}', '{self.age}', '{self.nationality}', '{self.websiteList}')"


class ModalData(db.Model):
    __tablename__ = 'modal_data'
    id = db.Column(db.Integer, primary_key=True)
    participantId = db.Column(db.Integer, db.ForeignKey('demographic_data.id'), nullable=False)
    currentWebsite = db.Column(db.String(50), nullable=False)
    consent = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f"modalData('{self.participantId}', '{self.id}', '{self.currentWebsite}', '{self.consent}')"


class ControlAndDeliberationData(db.Model):
    __tablename__ = 'control_and_deliberation_data'
    id = db.Column(db.Integer, primary_key=True)
    participantId = db.Column(db.Integer, db.ForeignKey('demographic_data.id'), nullable=False)
    currentWebsite = db.Column(db.String(50), nullable=False)
    perceivedControlQ1 = db.Column(db.Integer, nullable=False)
    perceivedControlQ2 = db.Column(db.Integer, nullable=False)
    perceivedControlQ3 = db.Column(db.Integer, nullable=False)
    perceivedControlQ4 = db.Column(db.Integer, nullable=False)
    perceivedControlQ5 = db.Column(db.Integer, nullable=False)
    manipulationCheck = db.Column(db.String(3), nullable=False)
    deliberation = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"controlAndDeliberationData('{self.participantId}', '{self.id}', '{self.currentWebsite}', '{self.perceivedControlQ1}', '{self.perceivedControlQ2}', '{self.perceivedControlQ3}', '{self.perceivedControlQ4}', '{self.perceivedControlQ5}', '{self.manipulationCheck}', '{self.deliberation}')"


class PrivacyConcernsData(db.Model):
    __tablename__ = 'privacy_concerns_data'
    id = db.Column(db.Integer, primary_key=True)
    participantId = db.Column(db.Integer, db.ForeignKey('demographic_data.id'), nullable=False)
    privacyConcernsQ1 = db.Column(db.String(1), nullable=False)
    privacyConcernsQ2 = db.Column(db.String(1), nullable=False)
    privacyConcernsQ3 = db.Column(db.String(1), nullable=False)
    correctDisplayed = db.Column(db.String(1), nullable=False)
    whichDevice = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"privacyConcernsData('{self.participantId}', '{self.id}', '{self.privacyConcernsQ1}', '{self.privacyConcernsQ2}', '{self.privacyConcernsQ3}', '{self.correctDisplayed}', '{self.whichDevice}')"
