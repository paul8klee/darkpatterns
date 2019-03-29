"""empty message

Revision ID: 4eb4eaa692b8
Revises: 
Create Date: 2019-03-29 11:29:45.087648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4eb4eaa692b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('demographic_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prolificID', sa.String(length=24), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('nationality', sa.String(length=50), nullable=False),
    sa.Column('websiteList', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('control_and_deliberation_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participantId', sa.Integer(), nullable=False),
    sa.Column('currentWebsite', sa.String(length=50), nullable=False),
    sa.Column('perceivedControlQ1', sa.Integer(), nullable=False),
    sa.Column('perceivedControlQ2', sa.Integer(), nullable=False),
    sa.Column('perceivedControlQ3', sa.Integer(), nullable=False),
    sa.Column('perceivedControlQ4', sa.Integer(), nullable=False),
    sa.Column('perceivedControlQ5', sa.Integer(), nullable=False),
    sa.Column('manipulationCheck', sa.String(length=3), nullable=False),
    sa.Column('deliberation', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['participantId'], ['demographic_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modal_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participantId', sa.Integer(), nullable=False),
    sa.Column('currentWebsite', sa.String(length=50), nullable=False),
    sa.Column('consent', sa.String(length=3), nullable=False),
    sa.ForeignKeyConstraint(['participantId'], ['demographic_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('privacy_concerns_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participantId', sa.Integer(), nullable=False),
    sa.Column('privacyConcernsQ1', sa.String(length=1), nullable=False),
    sa.Column('privacyConcernsQ2', sa.String(length=1), nullable=False),
    sa.Column('privacyConcernsQ3', sa.String(length=1), nullable=False),
    sa.Column('correctDisplayed', sa.String(length=1), nullable=False),
    sa.Column('whichDevice', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['participantId'], ['demographic_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('privacy_concerns_data')
    op.drop_table('modal_data')
    op.drop_table('control_and_deliberation_data')
    op.drop_table('demographic_data')
    # ### end Alembic commands ###